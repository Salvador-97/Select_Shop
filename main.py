from tkinter import *
from tkinter import ttk
from editPersonal import *
from configuracion import *

leerCSV()

# Ventana principal
app = Tk()
# app.geometry("700x600")
app.geometry("900x800")
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

icono = PhotoImage(file="icons/paquete.png")
app.iconphoto(False, icono)

# Pestañas
pestañas = ttk.Notebook(app)
pestañas.pack(fill='both', expand='yes')

pestañaPersonal = ttk.Frame(pestañas)
pestañaSSWMSOK = ttk.Frame(pestañas)
# pestañaTiempoExtra = ttk.Frame(pestañas)
pestañaConfiguracion = ttk.Frame(pestañas)

pestañas.add(pestañaPersonal, text='Personal')
pestañas.add(pestañaSSWMSOK, text='SSWMSOK')
# pestañas.add(pestañaTiempoExtra, text='Tiempo Extra')
pestañas.add(pestañaConfiguracion, text='Configuración')

# configuracionRutaArchivo()

obtenerPestañas(pestañaPersonal)
menuExcel(pestañaSSWMSOK)
menuConfiguracion(pestañaConfiguracion)

# guardarDatos(pestañaPersonal)

app.mainloop()