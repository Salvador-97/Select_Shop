from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext as scroll
import json
import csv
import re
from editSheet import *
from editExcel import *
from tools.manejarWidgets import *
from editPersonalExcel import *

def menuADIR(pestaña):
    
    labelProductos = Label(pestaña, text='Número de productos de ADIR', justify='center')
    labelProductos.pack()
    numeroProductos = ttk.Entry(pestaña, justify='center')
    numeroProductos.pack()
    
    
    
    # numeroProductosInt = int(numeroProductos.get())
    
    botonGenerar = ttk.Button(
        pestaña,
        text='Generar',
        command=lambda: generarEntradas(numeroProductos, pestaña)
    )
    
    botonGenerar.place(relx=0.45, rely=0.08)

def generarEntradas(numeroProductos, pestaña):
    
    numeroGenerar = int(numeroProductos.get())
    contador = 0.2
    
    labelCodigo = Label(pestaña, text='Codigo', justify='center')
    labelCodigo.place(relx=0.1, rely=0.2)
    
    labelEstiba = Label(pestaña, text='Estiba', justify='center')
    labelEstiba.place(relx=0.35, rely=0.2)
    
    labelTarimas = Label(pestaña, text='Tarimas', justify='center')
    labelTarimas.place(relx=0.5, rely=0.2)
    
    labelResto = Label(pestaña, text='Resto', justify='center')
    labelResto.place(relx=0.65, rely=0.2)
    
    codigos = [numeroProductos]
    estibas = [numeroProductos]
    tarimas = [numeroProductos]
    restos = [numeroProductos]
    
    for i in range(numeroGenerar):
        contador = contador + 0.05
        
        codigos[i] = ttk.Entry(pestaña, justify='center')
        codigos[i].place(relx=0.1, rely=contador, relwidth=0.2)
        
        estibas[i] = ttk.Entry(pestaña, justify='center')
        estibas[i].place(relx=0.35, rely=contador, relwidth=0.1)
        
        tarimas[i] = ttk.Entry(pestaña, justify='center')
        tarimas[i].place(relx=0.5, rely=contador, relwidth=0.1)
        
        restos[i] = ttk.Entry(pestaña, justify='center')
        restos[i].place(relx=0.65, rely=contador, relwidth=0.1)
    
    contador = 0.2