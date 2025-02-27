from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

def crearCampo(pestañaPersonal, texto, coordenadaX, coordenadaY, color):
    labelAux = customtkinter.CTkLabel(
        pestañaPersonal, 
        text=texto, 
        justify='center',
        font=('Aptos', 12, "bold"),
        text_color='#212529')
    labelAux.place(relx=coordenadaX, rely=coordenadaY)
    campoAux = customtkinter.CTkEntry(
        pestañaPersonal, 
        justify='center', 
        corner_radius=10, 
        fg_color=color,
        text_color='#495057',
        # font=('Aptos', 13, 'bold')
        )
    campoAux.place(relx=coordenadaX, rely=coordenadaY + 0.04)
    return campoAux

def habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
    barras.configure(state='normal')
    descripcion.configure(state='normal')
    estiba.configure(state='normal')
    noProductos.configure(state='normal')
    masterPack.configure(state='normal')
    
def deshabilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
     descripcion.configure(state='disabled')
     barras.configure(state='disabled')
     estiba.configure(state='disabled')
     noProductos.configure(state='disabled')
     masterPack.configure(state='disabled')


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