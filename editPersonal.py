import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext as scroll
import json
from editSheet import agregarDatos

def extrarNumero(codigo):
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
    
    labelBarras = Label(pestañaPersonal, text='Codigo de barras', justify='center')
    labelBarras.place(relx=0.2, rely=0.12)
    barras = ttk.Entry(pestañaPersonal, justify='center')
    barras.place(relx=0.2, rely=0.16)

    labelEstiba = Label(pestañaPersonal, text='Cajas por tarima', justify='center')
    labelEstiba.place(relx=0.6, rely=0.12)
    estiba = ttk.Entry(pestañaPersonal, justify='center')
    estiba.place(relx=0.6, rely=0.16)
    
    labelProductos = Label(pestañaPersonal, text='Productos por tarima', justify='center')
    labelProductos.place(relx=0.2, rely=0.22)
    noProductos = ttk.Entry(pestañaPersonal, justify='center')
    noProductos.place(relx=0.2, rely=0.26)
    
    labelMasterPack = Label(pestañaPersonal, text='Master Pack', justify='center')
    labelMasterPack.place(relx=0.6, rely=0.22)
    masterPack = ttk.Entry(pestañaPersonal, justify='center')
    masterPack.place(relx=0.6, rely=0.26)
    
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
    
def guardarDatos(pestañaPersonal):
    labelContenedor = Label(pestañaPersonal, text='Contenedor', justify='center')
    labelContenedor.place(relx=0.2, rely=0.54)
    campoContenedor = ttk.Entry(pestañaPersonal, justify='center')
    campoContenedor.place(relx=0.2, rely=0.58)
    
    labelFecha = Label(pestañaPersonal, text='Fecha', justify='center')
    labelFecha.place(relx=0.6, rely=0.54)
    campoFecha = ttk.Entry(pestañaPersonal, justify='center')
    campoFecha.place(relx=0.6, rely=0.58)
    
    labelProveedor = Label(pestañaPersonal, text='Proveedor', justify='center')
    labelProveedor.place(relx=0.2, rely=0.64)
    campoProveedor = ttk.Entry(pestañaPersonal, justify='center')
    campoProveedor.place(relx=0.2, rely=0.68)
    
    labelNoTarimas = Label(pestañaPersonal, text='Numero de tarimas', justify='center')
    labelNoTarimas.place(relx=0.6, rely=0.64)
    campoNoTarimas = ttk.Entry(pestañaPersonal, justify='center')
    campoNoTarimas.place(relx=0.6, rely=0.68)
    
    labelResto = Label(pestañaPersonal, text='Resto', justify='center')
    labelResto.place(relx=0.2, rely=0.74)
    campoResto = ttk.Entry(pestañaPersonal, justify='center')
    campoResto.place(relx=0.2, rely=0.78)
    
    botonAgregar = ttk.Button(
        pestañaPersonal, 
        text='Generar marbetes', 
        command=lambda: editarSheet(campoContenedor, campoNoTarimas, campoResto, campoFecha, campoProveedor))
    botonAgregar.place(relx=0.45, rely=0.84)
    
def editarSheet(contenedor, noTarimas, resto, fecha, proveedor):
    marbetes = []
    scrollPestaña = scroll.ScrolledText()
    marbetesGenerados = scroll.ScrolledText(pestañaPersonal, width=50, height=10)
    marbetesGenerados.place(relx=0.22, rely=0.90)
    listaDatos.append(contenedor.get())
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
    extrarNumero(codigoArticulo)

    if(articulosShop.get(codigoArticulo)):
        
        print('Se encontro la llave')
        listaInfoArticulo = articulosShop.get(codigoArticulo)
        informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack)
        listaDatos.append(campoCodigo.get())
        listaDatos.append(estiba.get())
        listaDatos.append(noProductos.get())
        listaDatos.append(descripcion.get())
        listaDatos.append(barras.get())
        listaDatos.append(masterPack.get())
        # print(listaDatos)
    else:
        print('No se encontro la llave')

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

# campoTexto = ttk.Entry(app)
# descripcion = ttk.Entry(app)
# barras = ttk.Entry(app)