from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def crearCampo(pestañaPersonal, texto, coordenadaX, coordenadaY):
    labelAux = Label(pestañaPersonal, text=texto, justify='center')
    labelAux.place(relx=coordenadaX, rely=coordenadaY)
    campoAux = ttk.Entry(pestañaPersonal, justify='center')
    campoAux.place(relx=coordenadaX, rely=coordenadaY + 0.04)
    return campoAux

def habilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
    barras.config(state='enabled')
    descripcion.config(state='enabled')
    estiba.config(state='enabled')
    noProductos.config(state='enabled')
    masterPack.config(state='enabled')
    
def deshabilitarEdicion(descripcion, barras, estiba, noProductos, masterPack):
     descripcion.config(state='disabled')
     barras.config(state='disabled')
     estiba.config(state='disabled')
     noProductos.config(state='disabled')
     masterPack.config(state='disabled')


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