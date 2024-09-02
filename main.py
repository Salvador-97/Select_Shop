from tkinter import *
from tkinter import ttk
from editPersonal import *

leerCSV()

# Ventana principal
app = Tk()
app.geometry("900x900")
app.title("Select Shop Inbound")
app.resizable(False, False)

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


# Button(pestañaPersonal, text='Hola')

pestañas.add(pestañaPersonal, text='Personal')
pestañas.add(pestañaTiempoExtra, text='Tiempo Extra')
# titulo.pack()

obtenerPestañas(pestañaPersonal)
guardarDatos(pestañaPersonal)

# iconoLupa = PhotoImage(file = r"icons/lupa.png")
# iconoLupa = iconoLupa.subsample(2)

# boton = ttk.Button(app, text='Buscar', width=25, command=verificacionInformacionArticulo)
# codigo.pack()

# boton.pack()
# descripcion.pack()
# barras.pack()
app.mainloop()

# link = input('Ingrese el id del archivo del drive')
# print('\n' + link)

