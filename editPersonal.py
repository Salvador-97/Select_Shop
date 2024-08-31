import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext as scroll
import json

def extrarNumero(codigo):
    numeros = leerNumerosMarbetes()
    codigoSKU = list(codigo)
    # print(codigoSKU)
    codigoAbreviado = codigoSKU[0] + codigoSKU[1]
    numero = numeros[codigoAbreviado]
    codigoMarbete.append(codigoAbreviado)
    codigoMarbete.append(numero)

def obtenerPestañas(pestaña):
    pestañaPersonal = pestaña
    columna1 = 250
    columna2 = 530
    
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
    # labelBarras.place(x=columna2, y=100)
    labelBarras.place(x=230, y=100)
    barras = ttk.Entry(pestañaPersonal, justify='center')
    barras.place(x=columna1 - 50, y=130)
    # barras.place(x=columna2 - 30, y=130)

    labelEstiba = Label(pestañaPersonal, text='Cajas por tarima', justify='center')
    # labelEstiba.pack()
    labelEstiba.place(x=columna2+8, y=100)
    estiba = ttk.Entry(pestañaPersonal, justify='center')
    estiba.place(x=columna2 - 30, y=130)
    # estiba.pack()
    
    labelProductos = Label(pestañaPersonal, text='Productos por tarima', justify='center')
    labelProductos.place(x=220, y=170)
    # labelProductos.pack()
    noProductos = ttk.Entry(pestañaPersonal, justify='center')
    noProductos.place(x=columna1 - 50, y=200)
    # noProductos.pack()
    
    labelMasterPack = Label(pestañaPersonal, text='Master Pack', justify='center')
    labelMasterPack.place(x=columna2+20, y=170)
    # labelMasterPack.pack()
    masterPack = ttk.Entry(pestañaPersonal, justify='center')
    masterPack.place(x=columna2 - 30, y=200)
    # masterPack.pack()
    
    labelDescripcion = Label(pestañaPersonal, text='Descripcion', justify='center')
    labelDescripcion.place(x=420, y=240)
    # labelDescripcion.pack()
    descripcion = ttk.Entry(pestañaPersonal, justify='center')
    descripcion.place(x=250, y=270, relwidth=0.5)
    # descripcion.pack()
    
    separator = ttk.Separator(pestañaPersonal, orient='horizontal')
    separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)

# def generarCampos():
#     campoCodigo = ttk.Entry(pestañaPersonal)
#     campoCodigo.pack()
#     boton = ttk.Button(pestañaPersonal, text='Nuevo')
#     boton.pack()

def informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack):
    if((barras.get() != '') or (descripcion.get() != '')):
        barras.config(state='enabled')
        barras.delete(0, END)
        
        descripcion.config(state='enabled')
        descripcion.delete(0, END)
        
        estiba.config(state='enabled')
        estiba.delete(0, END)
        
        noProductos.config(state='enabled')
        noProductos.delete(0, END)
        
        masterPack.config(state='enabled')
        masterPack.delete(0, END)
        
    descripcion.insert(0, listaInfoArticulo[0])
    # descripcion.config(state='disabled')
    barras.insert(0, listaInfoArticulo[1])
    barras.config(state='disabled')
    
    estiba.insert(0, listaInfoArticulo[2])
    estiba.config(state='disabled')
    
    noProductos.insert(0, listaInfoArticulo[3])
    noProductos.config(state='disabled')
    
    masterPack.insert(0, listaInfoArticulo[4])
    masterPack.config(state='disabled')
    # codigoMarbete = listaInfoArticulo[5]
    
def guardarDatos(pestañaPersonal):
    labelContenedor = Label(pestañaPersonal, text='Contenedor', justify='center')
    labelContenedor.place(x=250, y=400)
    # labelContenedor.pack()
    campoContenedor = ttk.Entry(pestañaPersonal, justify='center')
    campoContenedor.place(x=200, y=430)
    # campoContenedor.pack()
    
    labelNoTarimas = Label(pestañaPersonal, text='Numero de tarimas', justify='center')
    labelNoTarimas.place(x=515, y=400)
    # labelNoTarimas.pack()
    campoNoTarimas = ttk.Entry(pestañaPersonal, justify='center')
    campoNoTarimas.place(x=500, y=430)
    # campoNoTarimas.pack()
    
    labelResto = Label(pestañaPersonal, text='Resto', justify='center')
    # labelResto.pack()
    campoResto = ttk.Entry(pestañaPersonal, justify='center')
    # campoResto.pack()
    
    labelFecha = Label(pestañaPersonal, text='Fecha', justify='center')
    # labelFecha.pack()
    campoFecha = ttk.Entry(pestañaPersonal, justify='center')
    # campoFecha.pack()
    
    botonAgregar = ttk.Button(
        pestañaPersonal, 
        text='Agregar marbetes', 
        command=lambda: editarSheet(campoContenedor, campoNoTarimas, campoResto, campoFecha))
    # botonAgregar.pack()
    
def editarSheet(contenedor, noTarimas, resto, fecha):
    marbetes = []
    marbetesGenerados = scroll.ScrolledText(pestañaPersonal, width=50, height=10)
    marbetesGenerados.pack()
    print(noTarimas.get())
    # marbetesGenerados.grid(column = 0, pady = 10, padx = 10)
    
    for i in range(codigoMarbete[1], codigoMarbete[1] + int(noTarimas.get()), 1):
        marbetes.append(codigoMarbete[0] + str(i))
        # marbetesGenerados.tag_config("tag_name", justify='center')
        marbetesGenerados.insert(INSERT, codigoMarbete[0] + str(i) + '\n')
        print(codigoMarbete[0] + str(i))
    
    
    
    
def verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack):
    codigoArticulo = campoCodigo.get()
    extrarNumero(codigoArticulo)

    if(articulosShop.get(codigoArticulo)):
        
        print('Se encontro la llave')
        listaInfoArticulo = articulosShop.get(codigoArticulo)
        informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack)
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