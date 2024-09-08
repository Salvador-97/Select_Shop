from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext as scroll
import json
import csv
import re
from editSheet import agregarDatos

def crearCampo(texto, coordenadaX, coordenadaY):
    labelAux = Label(pestañaPersonal, text=texto, justify='center')
    labelAux.place(relx=coordenadaX, rely=coordenadaY)
    campoAux = ttk.Entry(pestañaPersonal, justify='center')
    campoAux.place(relx=coordenadaX, rely=coordenadaY + 0.04)
    return campoAux

def extraerNumero(codigo):
    numeros = leerNumerosMarbetes()
    codigoSKU = list(codigo)
    codigoAbreviado = codigoSKU[0] + codigoSKU[1]
    numero = numeros[codigoAbreviado]
    codigoMarbete.append(codigoAbreviado)
    codigoMarbete.append(numero)

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
    
    barras = crearCampo('Codigo de barras', 0.2, 0.16)
    estiba = crearCampo('Cajas por tarima', 0.6, 0.16)
    noProductos = crearCampo('Productos por tarima', 0.2, 0.26)
    masterPack = crearCampo('Master Pack', 0.6, 0.26)
    
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
    guardarDatos()

def obtenerNuevosDatos():
    listaDatos()


def habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
    barras.config(state='enabled')
    descripcion.config(state='enabled')
    estiba.config(state='enabled')
    noProductos.config(state='enabled')
    masterPack.config(state='enabled')
    
def deshabilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
     descripcion.config(state='disabled')
     barras.config(state='disabled')
     estiba.config(state='disabled')
     noProductos.config(state='disabled')
     masterPack.config(state='disabled')


def informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack):
    if((barras.get() != '') or (descripcion.get() != '')):
        habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack)
        barras.delete(0, END)
        descripcion.delete(0, END)
        estiba.delete(0, END)
        noProductos.delete(0, END)
        masterPack.delete(0, END)   
        
    descripcion.insert(0, listaInfoArticulo[0])
    barras.insert(0, listaInfoArticulo[1])
    estiba.insert(0, listaInfoArticulo[2])
    noProductos.insert(0, listaInfoArticulo[3])
    masterPack.insert(0, listaInfoArticulo[4])
    deshabilitarEdicion(descripcion, barras, estiba, noProductos, masterPack)
    # codigoMarbete = listaInfoArticulo[5]
    
def guardarDatos():
    
    contenedor = crearCampo('Contenedor', 0.2, 0.54)
    fecha = crearCampo('Fecha', 0.6, 0.54)
    proveedor = crearCampo('Proveedor', 0.2, 0.64)
    noTarimas = crearCampo('Numero de tarimas', 0.6, 0.64)
    resto = crearCampo('Resto', 0.2, 0.74)
    
    
    botonAgregar = ttk.Button(
        pestañaPersonal, 
        text='Generar marbetes', 
        command=lambda: editarSheet(contenedor, noTarimas, resto, fecha, proveedor))
    botonAgregar.place(relx=0.45, rely=0.84)
    
def editarSheet(contenedor, noTarimas, resto, fecha, proveedor):
    marbetes = []
    scrollPestaña = scroll.ScrolledText()
    marbetesGenerados = scroll.ScrolledText(pestañaPersonal, width=50, height=10)
    marbetesGenerados.place(relx=0.22, rely=0.90)
    
    listaDatos.append(codigoProducto)
    listaDatos.append(barras.get())
    listaDatos.append(estiba.get())
    listaDatos.append(noProductos.get())
    listaDatos.append(masterPack.get())
    listaDatos.append(descripcion.get())
    
    # listaDatos.append()
    listaDatos.append(noTarimas.get())
    listaDatos.append(resto.get())
    listaDatos.append(fecha.get())
    listaDatos.append(proveedor.get())
    print(listaDatos)
    # print(noTarimas.get())
    # marbetesGenerados.grid(column = 0, pady = 10, padx = 10)
    
    for i in range(codigoMarbete[1], codigoMarbete[1] + int(noTarimas.get()), 1):
        marbetes.append(codigoMarbete[0] + str(i))
        # marbetesGenerados.tag_config("tag_name", justify='center')
        marbetesGenerados.insert(INSERT, codigoMarbete[0] + str(i) + '\n')
        agregarDatos(codigoMarbete[0] + str(i), listaDatos)
    
def verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack):

    codigoArticulo = campoCodigo.get()
    codigoArticulo = codigoArticulo.upper()
    comprobacionRegex = '[A-Z][A-Z][1-9][0-9]*[0-9]*C[1-9][0-9]*'
    resultado = re.findall(comprobacionRegex, codigoArticulo)
    if(resultado):
        
        extraerNumero(codigoArticulo)

        if(articulosShop.get(codigoArticulo)):
            # print('Se encontro la llave')
            listaInfoArticulo = articulosShop.get(codigoArticulo)
            informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack)
            # codigoProducto = campoCodigo.get()
            # codigoBarras = barras
            # cajasTarimas = estiba
            # productosTarima = noProductos
            # masterPackCaja = masterPack
            # descripcionProducto = descripcion
            listaDatos.append(campoCodigo.get())
            # listaDatos.append(estiba.get())
            # listaDatos.append(noProductos.get())
            # listaDatos.append(descripcion.get())
            # listaDatos.append(barras.get())
            # listaDatos.append(masterPack.get())
            # print(listaDatos)
        else:
            messagebox.showwarning("Codigo no encontrado", "No se ha encontrado el producto")
    else:
        messagebox.showerror("Error", "Código no valido")

def leerCSV():
    with open('ArticulosSelectShop.csv') as articulos:
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
        numeros = json.load(archivoJSON)
    return numeros

articulosShop = {}
listaDatos = []
codigoMarbete = []
pestañaPersonal = None

codigoProducto = None
barras = None
estiba = None
noProductos = None
masterPack = None
descripcion = None