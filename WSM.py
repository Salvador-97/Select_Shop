import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from editExcel import *

def menuWSM(pestaña):
    """
    Pedir SKU, número de tarimas, inicio de ubicaciones asi como el final, opcion de si seran 4 o 5 espacios 
    a ocupar
    """
    labelCodigo = Label(pestaña, text='Codigo', justify='center')
    labelCodigo.place(relx=0.45, rely=0.05)
    
    labelnoTarimas = Label(pestaña, text='Tarimas', justify='center')
    labelnoTarimas.place(relx=0.1, rely=0.15)
    
    labelPasillo = Label(pestaña, text='Pasillo', justify='center')
    labelPasillo.place(relx=0.25, rely=0.15)
    
    labelUbicacionInicial = Label(pestaña, text='Inicio', justify='center')
    labelUbicacionInicial.place(relx=0.4, rely=0.15)
    
    labelUbicacionFinal = Label(pestaña, text='Final', justify='center')
    labelUbicacionFinal.place(relx=0.55, rely=0.15)
    
    labelEspacios = Label(pestaña, text='Espacios', justify='center')
    labelEspacios.place(relx=0.7, rely=0.15)
    
    codigo = ttk.Entry(pestaña, justify='center')
    codigo.place(relx=0.4, rely=0.1, relwidth=0.2)
        
    tarimas = ttk.Entry(pestaña, justify='center')
    tarimas.place(relx=0.1, rely=0.2, relwidth=0.1)
    
    pasillo = ttk.Entry(pestaña, justify='center')
    pasillo.place(relx=0.25, rely=0.2, relwidth=0.1)
    
    inicioUbicaciones = ttk.Entry(pestaña, justify='center')
    inicioUbicaciones.place(relx=0.4, rely=0.2, relwidth=0.1)
        
    finalUbicaciones = ttk.Entry(pestaña, justify='center')
    finalUbicaciones.place(relx=0.55, rely=0.2, relwidth=0.1)
    
    boxTarimas = tk.BooleanVar()
    checkbox = ttk.Checkbutton(pestaña, text="4 tarimas",
                          variable=boxTarimas)
    checkbox.place(relx=0.7, rely=0.2, relwidth=0.15)
    
    botonWSM = ttk.Button(
        pestaña,
        text='Agregar',
        command=lambda: generarUbicaciones(codigo, tarimas.get(), pasillo.get(), inicioUbicaciones.get(), finalUbicaciones.get(), boxTarimas)
    )
    
    botonWSM.place(relx=0.45, rely=0.3, relwidth=0.1)
    
def verficacionPasillo(boxTarimas):
    if boxTarimas.get():
        return 5
    else:
        return 6
    
    """
    El formato de los pasillos es P##0##A y de ahi se define si es impar o par
    """
def generarUbicaciones(codigoProducto, noTarimas, pasillo, inicio, final, boxTarimas):
    tarimasPasillo = verficacionPasillo(boxTarimas)
    contadorPasillos = 2
    contadorTarimas = 1
    letraA = 65
    
    residuoInicio = int(inicio) % 2
    residuoFinal = int(final) % 2

    if(residuoInicio == residuoFinal):
        for pasillos in range(int(inicio), int(final) + 1, contadorPasillos):
            contadorLetra = 0
            
            for espacios in range(1, tarimasPasillo):
                if(contadorTarimas != int(noTarimas) + 1):
                    if(pasillos < 100):
                        print(f'P{pasillo}0{pasillos}{chr(letraA + contadorLetra)}')
                    else:
                        print(f'P{pasillo}{pasillos}{chr(letraA + contadorLetra)}')
                    contadorLetra = contadorLetra + 1
                else:
                    break
                contadorTarimas = contadorTarimas + 1
    else:
        messagebox.showerror("Error", "Pasillos no compatibles.")
    