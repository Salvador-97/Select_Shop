from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv
from pathlib import Path
from editExcel import *
from tools.manejarWidgets import *
from PIL import Image, ImageTk

def configuracionRutaArchivo():
    if (bookPath == ''):
        messagebox.showwarning('Alerta', 'Seleccione un archivo para editar.')

def abrirArchivo():
    global ruta
    
    archivo = filedialog.askopenfilename(
        filetypes=(
            [("Excel files", ".xlsx .xls")]
        )
    )
    
    if archivo:
        ruta = archivoEditable(archivo)
    else:
        configuracionRutaArchivo()
    return ruta

def getRuta():
    return ruta

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
    labelConfig = customtkinter.CTkLabel(
        pestaña, text="Configuraciones", 
        justify='center', font=('Aptos', 13, 'bold'),
        text_color='#212529') 
    labelConfig.pack()
    
    archivoImagen = customtkinter.CTkImage(Image.open('icons\\file.png'), size=(15,15))

    labelArchivo = Label(pestaña, text='Archivo para personal')
    labelArchivo.place(relx=0.25, rely=0.10)
    archivo = customtkinter.CTkButton(
        pestaña, 
        text='Seleccionar archivo...', 
        command=abrirArchivo,
        image=archivoImagen,
        corner_radius=10,
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#184e77',
        text_color="white")
    archivo.place(relx=0.5, rely=0.10)

    labelArchivo = Label(pestaña, text='Archivo para \nentarimado de lote')
    labelArchivo.place(relx=0.25, rely=0.165)
    archivo = customtkinter.CTkButton(
        pestaña, 
        text='Seleccionar archivo...', 
        command=abrirArchivo,
        image=archivoImagen,
        corner_radius=10,
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#184e77',
        text_color="white")
    archivo.place(relx=0.5, rely=0.18)
    
    # labelArchivo = Label(pestaña, text='Link de Drive Personal')
    # labelArchivo.place(relx=0.4, rely=0.25)
    # archivo = ttk.Entry(pestaña)
    # archivo.place(relx=0.4, rely=0.3)
    
    separator = ttk.Separator(pestaña, orient='horizontal')
    separator.place(relx=0, rely=0.28, relwidth=1, relheight=1)
    
    labelProductoNuevo = customtkinter.CTkLabel(
        pestaña, text='Agregar nuevo producto',
        font=('Aptos', 13, 'bold'),
        text_color='#212529') 
    labelProductoNuevo.place(relx=0.38, rely=0.3)
    descripcion = customtkinter.CTkEntry(
        pestaña, justify='center',
        corner_radius=10,
        placeholder_text="SKU,Descripción,Código de Barras,Art. Tarima,Art. Estiba,Master Pack(N/A)",
        placeholder_text_color='#adb5bd',
        fg_color='white',
        border_width=1,
        state='normal')
    descripcion.place(relx=0.26, rely=0.35, relwidth=0.5)
    
    agregarImagen = customtkinter.CTkImage(Image.open('icons\\add.png'), size=(15,15))

    agregar = customtkinter.CTkButton(
        pestaña,
        text='Agregar',
        command=lambda: agregarProducto(descripcion.get()),
        image=agregarImagen,
        corner_radius=10,
        compound='right',
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#184e77',
        text_color='white'
    )
    agregar.place(relx=0.4, rely=0.42)
    
    
# pestañaConfiguracion = saludo()