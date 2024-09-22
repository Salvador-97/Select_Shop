from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from editExcel import archivoEditable

def abrirArchivo():
    archivo = filedialog.askopenfilename()
    
    if archivo:
        archivoEditable(archivo)
    else:
        print('No se ha seleccionado nada')

def menuConfiguracion(pestaña):
    labelConfig = Label(pestaña, text="Configuraciones", justify='center') 
    labelConfig.pack()
    
    labelArchivo = ttk.Button(
        pestaña, 
        text='Archivo a editar', 
        command=abrirArchivo)
    labelArchivo.pack()
    
    
# pestañaConfiguracion = saludo()