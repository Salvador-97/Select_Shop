import csv
from tkinter import *
from tkinter import ttk

def obtenerPestañas(pestañaPersonal):
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
    
    labelDescripcion = Label(pestañaPersonal, text='Descripcion', justify='center')
    labelDescripcion.pack()
    descripcion = ttk.Entry(pestañaPersonal, justify='center')
    descripcion.pack()
    
    labelBarras = Label(pestañaPersonal, text='Codigo de barras', justify='center')
    labelBarras.pack()
    barras = ttk.Entry(pestañaPersonal, justify='center')
    barras.pack()

    labelEstiba = Label(pestañaPersonal, text='Cajas por tarima', justify='center')
    labelEstiba.pack()
    estiba = ttk.Entry(pestañaPersonal, justify='center')
    estiba.pack()
    
    labelProductos = Label(pestañaPersonal, text='Productos por tarima', justify='center')
    labelProductos.pack()
    noProductos = ttk.Entry(pestañaPersonal, justify='center')
    noProductos.pack()
    
    labelMasterPack = Label(pestañaPersonal, text='Master Pack', justify='center')
    labelMasterPack.pack()
    masterPack = ttk.Entry(pestañaPersonal, justify='center')
    masterPack.pack()

# def generarCampos():
#     campoCodigo = ttk.Entry(pestañaPersonal)
#     campoCodigo.pack()
#     boton = ttk.Button(pestañaPersonal, text='Nuevo')
#     boton.pack()

def informacionArticulo(listaInfoArticulo, descripcion, barras, estiba, noProductos, masterPack):
    if(barras.get() != ''):
        barras.config(state='enabled')
        barras.delete(0, END)
        descripcion.delete(0, END)
        estiba.delete(0, END)
        noProductos.delete(0, END)
        masterPack.delete(0, END)
    descripcion.insert(0, listaInfoArticulo[0])
    # descripcion.config(state='disabled')
    barras.insert(0, listaInfoArticulo[1])
    barras.config(state='disabled')
    
    estiba.insert(0, listaInfoArticulo[2])
    
    noProductos.insert(0, listaInfoArticulo[3])
    
    masterPack.insert(0, listaInfoArticulo[4])
    
    
    
def verificacionInformacionArticulo(campoCodigo, descripcion, barras, estiba, noProductos, masterPack):
    codigoArticulo = campoCodigo.get()
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

articulosShop = {}

# campoTexto = ttk.Entry(app)
# descripcion = ttk.Entry(app)
# barras = ttk.Entry(app)