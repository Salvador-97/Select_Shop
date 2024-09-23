from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext as scroll
import json
import csv
import re
from editExcel import *
from tools.manejarWidgets import *
from editExcel import bookPath

# def crearCampo(pestañaPersonal, texto, coordenadaX, coordenadaY):
#     labelAux = Label(pestañaPersonal, text=texto, justify='center')
#     labelAux.place(relx=coordenadaX, rely=coordenadaY)
#     campoAux = ttk.Entry(pestañaPersonal, justify='center')
#     campoAux.place(relx=coordenadaX, rely=coordenadaY + 0.04)
#     return campoAux

def extraerNumero(codigo):
    numerosMarbetes = leerNumerosMarbetes()
    codigoSKU = list(codigo)
    codigoAbreviado = codigoSKU[0] + codigoSKU[1]
    numero = numerosMarbetes[codigoAbreviado]

    codigoMarbete[0] = codigoAbreviado
    codigoMarbete[1] = numero

def obtenerPestañas(pestaña):
    pestañaPersonal = pestaña
    
    labelCodigo = Label(pestañaPersonal, text='Codigo', justify='center')
    labelCodigo.pack()
    campoCodigo = ttk.Entry(pestañaPersonal, justify='center')
    campoCodigo.pack()
    
    boton = ttk.Button(
        pestañaPersonal, 
        text='Buscar', 
        command=lambda: verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack)
        )
    boton.pack()
    
    barras = crearCampo(pestañaPersonal, 'Codigo de barras', 0.2, 0.16)
    estiba = crearCampo(pestañaPersonal,'Productos por tarima', 0.6, 0.16)
    noProductos = crearCampo(pestañaPersonal,'Cajas por tarima', 0.2, 0.26)
    masterPack = crearCampo(pestañaPersonal,'Master Pack', 0.6, 0.26)
    
    labelDescripcion = Label(pestañaPersonal, text='Descripcion', justify='center')
    labelDescripcion.place(relx=0.45, rely=0.32)
    descripcion = ttk.Entry(pestañaPersonal, justify='center')
    descripcion.place(relx=0.26, rely=0.36, relwidth=0.5)
    
    botonEditar = ttk.Button(
        pestañaPersonal,
        text='Editar',
        command=lambda: habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack)
    )
    botonEditar.place(relx=0.45, rely=0.42)
        
    separator = ttk.Separator(pestañaPersonal, orient='horizontal')
    separator.place(relx=0, rely=0.5, relwidth=1, relheight=1)
    guardarDatos(pestañaPersonal, campoCodigo, barras, estiba, noProductos, masterPack, descripcion)
    
def guardarDatos(pestañaPersonal, campoCodigo, barras, estiba, noProductos, masterPack, descripcion):
    
    contenedor = crearCampo(pestañaPersonal, 'Contenedor', 0.2, 0.54)
    fecha = crearCampo(pestañaPersonal, 'Fecha', 0.6, 0.54)
    proveedor = crearCampo(pestañaPersonal, 'Proveedor', 0.2, 0.64)
    noTarimas = crearCampo(pestañaPersonal, 'Numero de tarimas', 0.6, 0.64)
    resto = crearCampo(pestañaPersonal, 'Resto', 0.2, 0.74)
    ubicacion = crearCampo(pestañaPersonal, 'Ubicación', 0.6, 0.74)
    
    botonAgregar = ttk.Button(
        pestañaPersonal, 
        text='Generar marbetes', 
        command=lambda: editarSheet(contenedor, noTarimas, resto, fecha, proveedor, 
                                    campoCodigo, barras, estiba, noProductos, masterPack, descripcion, ubicacion))
    botonAgregar.place(relx=0.42, rely=0.84)
    
def validacionDatos(expresionRegular, campoVerificar):
    campoMayus = campoVerificar.get().upper()
    resultado = re.findall(expresionRegular, campoMayus)
    if(resultado):
        listaDatos.append(campoMayus)
        validacionCampos = True
    else:
        validacionCampos = False
    return validacionCampos

def editarSheet(contenedor, noTarimas, resto, fecha, proveedor, 
                campoCodigo, barras, estiba, noProductos, masterPack, descripcion, ubicacion):
    if (ruta() == ''):
        messagebox.showwarning('Alerta', 'Seleccione un archivo para editar.')
    else:
        marbetes = []
        validacionCampos = []
        
        listaDatos.append(campoCodigo.get().upper())
        listaDatos.append(estiba.get())
        listaDatos.append(noProductos.get())
        listaDatos.append(descripcion.get())
        listaDatos.append(barras.get())
        listaDatos.append(masterPack.get())
        
        validacionCampos.append(validacionDatos('[0-9][0-9]*[0-9]*', noTarimas))
        validacionCampos.append(validacionDatos('[0-9][0-9]*[0-9]*', resto))
        validacionCampos.append(validacionDatos('(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}', fecha))    
        validacionCampos.append(validacionDatos('[A-Z][0-9][0-9][0-9]', proveedor))    
        validacionCampos.append(validacionDatos('[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', contenedor))
        validacionCampos.append(validacionDatos('[A-Z][1-9][0-9]*A[1-9][0-9]*', ubicacion))
            
        if(validacionCampos.count(False) == 0):
            # print(f'BookPath: {bookPath}')
            indiceFinal = codigoMarbete[1] + int(noTarimas.get())
            # contador = 1
            for i in range(codigoMarbete[1], indiceFinal, 1):
                marbetes.append(codigoMarbete[0] + str(i))
                
                if((i == indiceFinal - 1) and (resto.get() != '0')):
                    if((masterPack.get() != 'N/A') and (resto.get() != '0')):
                        listaDatos[1] = int(masterPack.get()) * int(resto.get())
                        listaDatos[7] = listaDatos[1]
                        listaDatos[2] = resto.get()
                        # print(listaDatos)
                        editarExcel(listaDatos)
                    else:
                        listaDatos[1] = listaDatos[7]
                        listaDatos[2] = listaDatos[7]
                        editarExcel(listaDatos)
                else:
                    editarExcel(listaDatos)
                # contador = contador + 1
            messagebox.showinfo("Marbetes", "Marbetes generados exitosamente")
            codigoMarbete[1] = codigoMarbete[1] + int(noTarimas.get())
            numerosMarbetes = leerNumerosMarbetes()
            actualizarJSON(numerosMarbetes, codigoMarbete[0], int(noTarimas.get()))
            listaDatos.clear()
            guardarExcel()
        else:
            messagebox.showerror('Error', 'Dato erróneo, verificar campos')
        cerrarExcel()   
    
def verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack):

    codigoArticulo = campoCodigo.get()
    codigoArticulo = codigoArticulo.upper()
    comprobacionRegex = '[A-Z][A-Z][1-9][0-9]*[0-9]*C[1-9][0-9]*'
    resultado = re.findall(comprobacionRegex, codigoArticulo)
    
    if(resultado):
        
        extraerNumero(codigoArticulo)

        if(articulosShop.get(codigoArticulo)):
            listaInfoArticulo = articulosShop.get(codigoArticulo)
            informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack)
        else:
            messagebox.showwarning("Codigo no encontrado", "No se ha encontrado el producto")
    else:
        messagebox.showerror("Error", "Código no valido")

def leerCSV():
    with open('files/ArticulosSelectShop.csv') as articulos:
        csv_reader = csv.reader(articulos, delimiter = ',')
        next(csv_reader)
        
        for fila in csv_reader:
            listaInformacion = [fila[1], fila[2], fila[3], fila[4], fila[5]]
            diccionarioAux = {fila[0]: listaInformacion}
            articulosShop.update(diccionarioAux)
            diccionarioAux = {}
            listaInformacion = []
            
def leerNumerosMarbetes():
    with open("files/marbetesNumeros.json") as archivoJSON:
        numerosExtraidos = json.load(archivoJSON)
    archivoJSON.close()
    return numerosExtraidos

def actualizarJSON(numeros, key, aumento):
    if key in numeros:
        numeros[key] = numeros[key] + aumento
        with open("files/marbetesNumeros.json", "w") as archivoJSONedit:
            json.dump(numeros, archivoJSONedit)
        archivoJSONedit.close()

articulosShop = {}
listaDatos = []
codigoMarbete = ['', 0]

# pestañaPersonal = None