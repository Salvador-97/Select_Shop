from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext as scroll
import customtkinter 
import json
import csv
import re
from editSheet import *
from editExcel import *
from configuracion import *
from tools.manejarWidgets import *
from editPersonalExcel import *
from PIL import Image, ImageTk

def extraerNumero(codigo):
    """
    Función que extrae los primeros dos caracteres del código ingresado por el usuario. 
    Seguido de esto los concatena y lo busca en la lista del registro de marbetes.
    Por último, guarda el la categoria del producto (HG, EL, PO...) y el número
    del último marbete generado para esa categoria.
    """
    
    if(codigo != ''):
        numerosMarbetes = leerNumerosMarbetes()
        codigoSKU = list(codigo)
        

        if(str(codigo).startswith('ADIR')):
            codigoAbreviado = 'ADIR'
        else:
            codigoAbreviado = codigoSKU[0] + codigoSKU[1]

        if(numerosMarbetes.get(codigoAbreviado)):
            numero = numerosMarbetes[codigoAbreviado]
            codigoMarbete[0] = codigoAbreviado
            codigoMarbete[1] = numero
    else:
        messagebox.showwarning('Alerta', 'Código no ingresado.')
    #Agregar funcion de verificacion de la clave en JSON de marbetes
    

def obtenerPestañas(pestaña):
    """
    Genera todos los widgets de la pestaña para generar marbetes, mostrando cada uno de los 
    campos que obtiene de buscar un código de un producto, dando la opción de poder editar
    dichos campos.
    """
    pestañaPersonal = pestaña
    
    labelCodigo = generarLabel(pestaña, 'Código (SKU)')
    labelCodigo.pack()
    campoCodigo = generarEntry(pestaña, 'white')
    campoCodigo.pack()

    lupaImagen = customtkinter.CTkImage(Image.open('icons\Lupa.png'), size=(15,15))

    boton = customtkinter.CTkButton(
        pestañaPersonal, 
        text='Buscar', 
        command=lambda: verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack),
        corner_radius=10,
        width=100,
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#184e77',
        image=lupaImagen, 
        compound='right'
        )
    boton.pack(padx=10, pady=10)
    
    barras = crearCampo(pestañaPersonal, 'Código de barras', 0.2, 0.16, '#dee2e6')
    estiba = crearCampo(pestañaPersonal,'Productos por tarima', 0.6, 0.16, '#dee2e6')
    noProductos = crearCampo(pestañaPersonal,'Cajas por tarima', 0.2, 0.26, '#dee2e6')
    masterPack = crearCampo(pestañaPersonal,'Master Pack', 0.6, 0.26, '#dee2e6')
    
    labelDescripcion = generarLabel(pestaña, 'Descripción')
    labelDescripcion.place(relx=0.45, rely=0.35)
    descripcion = generarEntry(pestaña, 'white')
    descripcion.place(relx=0.26, rely=0.39, relwidth=0.5)
    
    editarImagen = customtkinter.CTkImage(Image.open('icons\pen.png'), size=(15,15))

    botonEditar = customtkinter.CTkButton(
        pestañaPersonal,
        text='Editar',
        command=lambda: habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack),
        corner_radius=10,
        width=100,
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#184e77',
        image=editarImagen,
        compound='right'
    )
    botonEditar.place(relx=0.42, rely=0.45)
        
    separator = ttk.Separator(pestañaPersonal, orient='horizontal')
    separator.place(relx=0, rely=0.52, relwidth=1, relheight=1)
    guardarDatos(pestañaPersonal, campoCodigo, barras, estiba, noProductos, masterPack, descripcion)
    
def guardarDatos(pestañaPersonal, campoCodigo, barras, estiba, noProductos, masterPack, descripcion):
    """
    Crea los widgets de lo que ingresara el usuario para generar los marbetes
    """
    contenedor = crearCampo(pestañaPersonal, 'Contenedor', 0.2, 0.54, 'white')
    fecha = crearCampo(pestañaPersonal, 'Fecha', 0.6, 0.54, 'white')
    proveedor = crearCampo(pestañaPersonal, 'Proveedor', 0.2, 0.64, 'white')
    noTarimas = crearCampo(pestañaPersonal, 'Número de tarimas', 0.6, 0.64, 'white')
    resto = crearCampo(pestañaPersonal, 'Resto (Cajas)', 0.2, 0.74, 'white')
    # ubicacion = crearCampo(pestañaPersonal, 'Ubicación', 0.6, 0.74, 'white')
    
    generarImagen = customtkinter.CTkImage(Image.open('icons\gears.png'), size=(15,15))

    botonAgregar = customtkinter.CTkButton(
        pestañaPersonal, 
        text='Generar', 
        command=lambda: editarSheet(contenedor, noTarimas, resto, fecha, proveedor, 
                                    campoCodigo, barras, estiba, noProductos, masterPack, descripcion),
        corner_radius=10,
        width=100,
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#29bf12',
        image=generarImagen,
        compound='right')
    botonAgregar.place(relx=0.42, rely=0.87)
    
def validacionDatos(expresionRegular, campoVerificar):
    """Revisa el campo ingresado por el usuario a partir de una expresión regular
    para así asegurar que los datos sean correctos"""
    campoMayus = campoVerificar.get().upper()
    resultado = re.findall(expresionRegular, campoMayus)
    if(resultado):
        listaDatos.append(campoMayus)
        validacionCampos = True
        campoVerificar.configure(fg_color='white', text_color='#495057')
    else:
        validacionCampos = False
        campoVerificar.configure(fg_color='#f21b3f', text_color='#eff1ed')
    return validacionCampos

def editarSheet(contenedor, noTarimas, resto, fecha, proveedor, 
                campoCodigo, barras, estiba, noProductos, masterPack, descripcion):
    """
    Obtiene los datos ingresados por el usuario y los agrega al archivo de Drive y Excel siempre 
    y cuando los datos sean correctos.
    """
    
    if(campoCodigo.get() != ''):
        marbetes = []
        validacionCampos = []
            
        indiceFinal = codigoMarbete[1] + int(noTarimas.get())
        listaDatos.append(campoCodigo.get().upper())
        listaDatos.append(estiba.get())
        listaDatos.append(noProductos.get())
        listaDatos.append(descripcion.get())
        listaDatos.append(barras.get())
        listaDatos.append(masterPack.get())
            
        validacionCampos.append(validacionDatos('[0-9][0-9]*[0-9]*', noTarimas))
        validacionCampos.append(validacionDatos('[0-9][0-9]*[0-9]*', resto))
        validacionCampos.append(validacionDatos('(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}', fecha))    
        validacionCampos.append(validacionDatos('P0[0-9][0-9]', proveedor))    
        validacionCampos.append(validacionDatos('[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', contenedor))
        # validacionCampos.append(validacionDatos('[A-Z][1-9][0-9]*A[1-9][0-9]*', ubicacion))
                
        if(validacionCampos.count(False) == 0):
            
            pathArchivoPersonal = ruta()
            
            if(pathArchivoPersonal):
            
                for i in range(codigoMarbete[1], indiceFinal, 1):
                    marbetes.append(codigoMarbete[0] + str(i))
                    """
                    Cuando llega a la última posición verifica el valor del resto
                    para para agregar esa cantidad en la columna correspondiente, en caso de que
                    el producto sea Master Pack se realiza la operación para calcular el total
                    de piezas
                    """
                    if((i == indiceFinal - 1) and (resto.get() != '0')):
                        if((masterPack.get() != 'N/A') and (resto.get() != '0')):
                            listaDatos[1] = int(masterPack.get()) * int(resto.get())
                            listaDatos[7] = listaDatos[1]
                            listaDatos[2] = resto.get()
                            #editarArchivoExcel(listaDatos)
                            #agregarDatos(codigoMarbete[0] + str(i), listaDatos)
                            editMarbetes(codigoMarbete[0] + str(i), listaDatos)
                        else:
                            listaDatos[1] = listaDatos[7]
                            listaDatos[2] = listaDatos[7]
                            #editarArchivoExcel(listaDatos)
                            #agregarDatos(codigoMarbete[0] + str(i), listaDatos)
                            editMarbetes(codigoMarbete[0] + str(i), listaDatos)
                    else:
                        #editarArchivoExcel(listaDatos)
                        #agregarDatos(codigoMarbete[0] + str(i), listaDatos)
                        editMarbetes(codigoMarbete[0] + str(i), listaDatos)   
                messagebox.showinfo("Marbetes", "Marbetes generados exitosamente")
                codigoMarbete[1] = codigoMarbete[1] + int(noTarimas.get())
                numerosMarbetes = leerNumerosMarbetes()
                actualizarJSON(numerosMarbetes, codigoMarbete[0], int(noTarimas.get()))
                listaDatos.clear()
                #guardarExcel()
                guardarExcelMarbete()
            else:
                pathArchivoPersonal = abrirArchivo()
                abrirLibro(pathArchivoPersonal)
            cerrarExcelMarbete()
        else:
            messagebox.showerror('Error', 'Dato erróneo, verificar campos')
            listaDatos.clear()
                #cerrarExcel()
    else:
        messagebox.showerror('Error', 'No se pueden generar información.\nBusque un producto.')    
    
def verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack):
    """
    Verifica que el código ingresado por el usuario conrresponda con el formato establecido de los 
    códigos de los productos
    """
    #Agregar expresion para ADIR y productos faltantes
    codigoArticulo = campoCodigo.get()
    codigoArticulo = codigoArticulo.upper()
    comprobacionRegex = '[A-Z][A-Z][1-9][0-9]*[0-9]*C[1-9][0-9]*'
    comprobacionRegexADIR = 'ADIR[0-9][0-9]*[0-9]*[0-9]*[0-9]*[0-9]*[0-9]*'
    resultado = re.findall(comprobacionRegex, codigoArticulo)
    resultadoADIR = re.findall(comprobacionRegexADIR, codigoArticulo)
    
    if((resultado != '') or (resultadoADIR != '')):
        
        extraerNumero(codigoArticulo)

        if(articulosShop.get(codigoArticulo)):
            listaInfoArticulo = articulosShop.get(codigoArticulo)
            listaInfoArticulo[0] = listaInfoArticulo[0].decode('utf-8')
            campoCodigo.configure(fg_color='#affc41', text_color='#495057')
            informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack)
        else:
            if(codigoArticulo != ''):
                messagebox.showwarning("Código no encontrado", "No se ha encontrado el producto\nIntente de nuevo")
                campoCodigo.configure(fg_color='#ffd449', text_color='#495057')
    else:
        messagebox.showerror("Error", "Código no válido")
        campoCodigo.configure(fg_color='#f21b3f', text_color='#eff1ed')

# -*- coding: utf-8 -*-
def leerCSV():
    """
    Lee el archivo de todos los productos para generar una lista que servira como consulta
    """
    #Agregar excepcion en caso de que no se pueda abrir o leer el archivo
    with open('files/ArticulosSelectShop.csv', 'r', encoding='utf-8') as articulos:
        csv_reader = csv.reader(articulos, delimiter = ',')
        next(csv_reader)
        
        for fila in csv_reader:
            listaInformacion = [
                fila[1].encode('utf-8'), 
                fila[2].encode('utf-8'), 
                fila[3].encode('utf-8'), 
                fila[4].encode('utf-8'), 
                fila[5].encode('utf-8')]
            diccionarioAux = {fila[0]: listaInformacion}
            articulosShop.update(diccionarioAux)
            diccionarioAux = {}
            listaInformacion = []
def leerNumerosMarbetes():
    """
    Abre el archivo de los contadores de cada una de las categorias de los productos
    """
    with open("files/marbetesNumeros.json") as archivoJSON:
        numerosExtraidos = json.load(archivoJSON)
    archivoJSON.close()
    return numerosExtraidos

def actualizarJSON(numeros, key, aumento):
    """
    Abre y edita el archivo de los contadores de cada una de las catergorias de lo productos
    """
    if key in numeros:
        numeros[key] = numeros[key] + aumento
        with open("files/marbetesNumeros.json", "w") as archivoJSONedit:
            json.dump(numeros, archivoJSONedit)
        archivoJSONedit.close()

articulosShop = {}
listaDatos = []
codigoMarbete = ['', 0]
