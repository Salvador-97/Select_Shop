from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv
from pathlib import Path
from editExcel import *
from tools.manejarWidgets import *

def configuracionRutaArchivo():
    if (bookPath == ''):
        messagebox.showwarning('Alerta', 'Seleccione un archivo para editar.')

def abrirArchivo():
    archivo = filedialog.askopenfilename(
        filetypes=(
            [("Excel files", ".xlsx .xls")]
        )
    )
    
    if archivo:
        archivoEditable(archivo)
    else:
        configuracionRutaArchivo()

def editarCSVNuevoProducto(informacionProducto):
    columnas = ['codigo', 'Nombre', 'Barras', 'Tarima', 'Estiba', 'masterPack']
    with open('files/ArticulosSelectShop.csv', 'a', encoding='utf-8', newline="") as articulos:
        writer = csv.writer(articulos)
        writer.writerow(informacionProducto)

def agregarProducto(producto):
    informacionProducto = producto.split(',')
    codigoEncontrado = False
   
    with open('files/ArticulosSelectShop.csv', 'r', encoding='utf-8') as articulos:
        csv_reader = csv.reader(articulos, delimiter = ',')
        next(csv_reader)
        
        for fila in csv_reader:
            if(fila == informacionProducto):
                # print("El producto ya se encuentra registrado")
                codigoEncontrado = True
                messagebox.showwarning("Código encontrado", "El producto ya se encuentra registrado")
                break
            else:
                codigoEncontrado = False
                # print("Articulo agregado correctamente")
    articulos.close()
                
    if(codigoEncontrado == False):
        editarCSVNuevoProducto(informacionProducto)

def menuConfiguracion(pestaña):
    # crearCampo(pestaña, 'Configuraciones', )
    labelConfig = Label(pestaña, text="Configuraciones", justify='center') 
    labelConfig.pack()
    
    labelArchivo = Label(pestaña, text='Archivo para entarimado de lote')
    labelArchivo.place(relx=0.36, rely=0.1)
    archivo = ttk.Button(
        pestaña, 
        text='Seleccionar archivo...', 
        command=abrirArchivo)
    archivo.place(relx=0.4, rely=0.15)
    
    labelArchivo = Label(pestaña, text='Link de Drive Personal')
    labelArchivo.place(relx=0.4, rely=0.25)
    archivo = ttk.Entry(pestaña)
    archivo.place(relx=0.4, rely=0.3)
    
    separator = ttk.Separator(pestaña, orient='horizontal')
    separator.place(relx=0, rely=0.5, relwidth=1, relheight=1)
    
    labelProductoNuevo = Label(pestaña, text='Agregar nuevo producto')
    labelProductoNuevo.place(relx=0.4, rely=0.55)
    descripcion = ttk.Entry(pestaña, justify='center')
    descripcion.place(relx=0.28, rely=0.6, relwidth=0.5)
    
    agregar = ttk.Button(
        pestaña,
        text='Agregar',
        command=lambda: agregarProducto(descripcion.get())
    )
    agregar.place(relx=0.45, rely=0.65)
    
    
# pestañaConfiguracion = saludo()