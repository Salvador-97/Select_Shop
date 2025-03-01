import openpyxl
from openpyxl import workbook
from openpyxl.styles import *

def abrirLibro(ruta):
    global book
    book = openpyxl.load_workbook(ruta)
    
def editMarbetes(marbete, listaDatos):
    #Agregar opcion de elegir la pestaña del archivo de excel

    sheet = book['Personal']

    columnaA = sheet.column_dimensions['A']
    columnaA.alignment = Alignment(horizontal='center', vertical='center')

    if(listaDatos[5] != 'N/A'):
        listaDatos[5] = int(listaDatos[5])

    nuevaFila = [marbete, listaDatos[0], '', int(listaDatos[1]), int(listaDatos[2]), '', listaDatos[3], listaDatos[8], listaDatos[10],
               listaDatos[3], int(listaDatos[4]), listaDatos[5], listaDatos[9]]
               
    sheet.append(nuevaFila)
    
def guardarExcelMarbete():
    book.save('files/Pruebas_Excel.xlsx')
    
def cerrarExcelMarbete():
    book.close()