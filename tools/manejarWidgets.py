from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

def generarLabel(pestaña, texto):
    labelTemp = customtkinter.CTkLabel(
        pestaña, 
        text=texto, 
        justify='center',
        font=('Aptos', 12, "bold"),
        text_color='#212529')
    return labelTemp

def generarEntry(pestaña, color):
    entryTemp = customtkinter.CTkEntry(
        pestaña, 
        justify='center', 
        corner_radius=6, 
        fg_color=color,
        text_color='#495057',
        border_width=1
        # font=('Aptos', 13, 'bold')
        )
    return entryTemp

def generarBoton(pestaña, funcion, imagen):
    botonTemp = customtkinter.CTkButton(
        pestaña, 
        text='Buscar', 
        command=lambda: funcion,
        corner_radius=10,
        width=100,
        font=('Aptos', 13, "bold"),
        fg_color='#168aad',
        hover_color='#184e77',
        image=imagen, 
        compound='right'
        )
    return botonTemp

def crearCampo(pestañaPersonal, texto, coordenadaX, coordenadaY, color):
    labelAux = generarLabel(pestañaPersonal, texto)
    labelAux.place(relx=coordenadaX, rely=coordenadaY)
    campoAux = generarEntry(pestañaPersonal, color)
    campoAux.place(relx=coordenadaX, rely=coordenadaY + 0.04)
    return campoAux

def habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
    barras.configure(state='normal', fg_color='white')
    descripcion.configure(state='normal', fg_color='white')
    estiba.configure(state='normal', fg_color='white')
    noProductos.configure(state='normal', fg_color='white')
    masterPack.configure(state='normal', fg_color='white')
    
def deshabilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
     descripcion.configure(state='disabled', fg_color='#dee2e6')
     barras.configure(state='disabled', fg_color='#dee2e6')
     estiba.configure(state='disabled', fg_color='#dee2e6')
     noProductos.configure(state='disabled', fg_color='#dee2e6')
     masterPack.configure(state='disabled', fg_color='#dee2e6')


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