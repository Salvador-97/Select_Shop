from gui.ventana import crearVentana
from gui.pestañas import crearPestaña, crearPestañas
from editPersonal import *
from configuracion import *
from editAdir import *
from WSM import *

def main():
    leerCSV()
    # Ventana principal
    app = crearVentana("Select Shop Inbound", "600x600")

    app.update()

    # altura_pantalla = app.winfo_screenheight()
    # anchura_pantalla = app.winfo_screenwidth()
    # print(f"Altura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")

    # Pestañas
    pestañaPrincipal = crearPestaña(app)
    
    pestañaPersonal  = crearPestañas(pestañaPrincipal, 'Personal')
    pestañaConfiguracion = crearPestañas(pestañaPrincipal, 'Configuración')
    
    # pestañaSSWMSOK = ttk.Frame(pestañas)
    # pestañaTiempoExtra = ttk.Frame(pestañas)
    # pestañaConfiguracion = ttk.Frame(pestañas)
    # pestañaAdir = ttk.Frame(pestañas)


    
    # pestañas.add(pestañaAdir, text='ADIR')
    # pestañas.add(pestañaSSWMSOK, text='SSWMSOK')
    # pestañas.add(pestañaTiempoExtra, text='Tiempo Extra')
    # pestañas.add(pestañaConfiguracion, text='Configuración')


    # configuracionRutaArchivo()

    obtenerPestañas(pestañaPersonal)
    # menuExcel(pestañaSSWMSOK)
    # menuConfiguracion(pestañaConfiguracion)
    # menuADIR(pestañaAdir)
    # menuWSM(pestañaSSWMSOK)

    # guardarDatos(pestañaPersonal)

    app.mainloop()

if __name__ == "__main__":
    main()