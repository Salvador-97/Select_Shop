from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from editExcel import *

def configuracionRutaArchivo():
    if (bookPath == ''):
        messagebox.showwarning('Alerta', 'Seleccione un archivo para editar.')

def abrirArchivo():
    archivo = filedialog.askopenfilename()
    
    if archivo:
        archivoEditable(archivo)
    else:
        configuracionRutaArchivo()

def menuConfiguracion(pestaña):
    labelConfig = Label(pestaña, text="Configuraciones", justify='center') 
    labelConfig.pack()
    
    labelArchivo = ttk.Button(
        pestaña, 
        text='Archivo a editar', 
        command=abrirArchivo)
    labelArchivo.pack()
    
    botonLimpiar = ttk.Button(
        pestaña,
        text='Limpiar',
        command=reiniciarContador()
    )
    botonLimpiar.pack()
    
# pestañaConfiguracion = saludo()