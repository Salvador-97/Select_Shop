import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage


def crearVentana(titulo, dimensiones):
    app = ctk.CTk()
    app.geometry(dimensiones)
    app.title(titulo)
    app.resizable(False, False)
    
    icono = PhotoImage(file="icons/paquete.png")
    app.iconphoto(False, icono)
    
    return app