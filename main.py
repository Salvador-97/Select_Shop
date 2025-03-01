from tkinter import *
from tkinter import ttk
from editPersonal import *
from configuracion import *
from editAdir import *
from WSM import *
import customtkinter 

leerCSV()

# Ventana principal
app = customtkinter.CTk()
# customtkinter.set_default_color_theme("green") 
app.geometry("600x600")
app.title("Select Shop Inbound")
app.resizable(False, False)

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
# pestañaAdir = ttk.Frame(pestañas)


pestañas.add(pestañaPersonal, text='Personal')
# pestañas.add(pestañaAdir, text='ADIR')
pestañas.add(pestañaSSWMSOK, text='SSWMSOK')
# pestañas.add(pestañaTiempoExtra, text='Tiempo Extra')
pestañas.add(pestañaConfiguracion, text='Configuración')


# configuracionRutaArchivo()

obtenerPestañas(pestañaPersonal)
# menuExcel(pestañaSSWMSOK)
menuConfiguracion(pestañaConfiguracion)
# menuADIR(pestañaAdir)
menuWSM(pestañaSSWMSOK)

# guardarDatos(pestañaPersonal)

app.mainloop()