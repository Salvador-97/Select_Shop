from tkinter import *
from tkinter import ttk
from editPersonal import *

leerCSV()

# Ventana principal
app = Tk()
app.geometry("900x900")
app.title("Select Shop Inbound")
# app.resizable(False, False)

app.update()

# altura_pantalla = app.winfo_screenheight()
# anchura_pantalla = app.winfo_screenwidth()
# print(f"Altura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")

titulo = Label(app, text='Inbound Manager')
codigo = Label(
    app,
    text='Codigo',
    justify='center',
)

# Pestañas
pestañas = ttk.Notebook(app)
pestañas.pack(fill='both', expand='yes')

pestañaPersonal = ttk.Frame(pestañas)
pestañaTiempoExtra = ttk.Frame(pestañas)

pestañas.add(pestañaPersonal, text='Personal')
pestañas.add(pestañaTiempoExtra, text='Tiempo Extra')

obtenerPestañas(pestañaPersonal)
guardarDatos(pestañaPersonal)

app.mainloop()