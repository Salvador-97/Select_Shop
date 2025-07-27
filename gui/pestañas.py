import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from customtkinter import CTkTabview

def crearPestaña(app):
    pestaña = ttk.Notebook(app)
    pestaña.pack(fill='both', expand='yes')
    return pestaña

def crearPestañas(pestañaPrincipal, nombre):
    pestañaNueva = tk.Frame(pestañaPrincipal)
    pestañaPrincipal.add(pestañaNueva, text=nombre)
    # pestañas = ctk.CTkTabview(app)
    # pestañas.pack(padx=20, pady=20)
    
    # pestañas.add(nombre)
    # button_1 = ctk.CTkButton(pestañas.tab(nombre))
    # button_1.pack(padx=20, pady=20)
    
    return pestañaNueva