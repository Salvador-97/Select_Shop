from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
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
    
# pestañaConfiguracion = saludo()