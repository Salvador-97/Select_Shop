import openpyxl

def editMarbetes(marbete, listaDatos):
    #Agregar opcion de elegir la pestaña del archivo de excel
    global book
    book = openpyxl.load_workbook('files/Pruebas_Excel.xlsx')
    sheet = book['Prueba']
    nuevaFila = [marbete, listaDatos[0], '', listaDatos[1], listaDatos[2], '', listaDatos[3], listaDatos[8], listaDatos[10],
               listaDatos[3], listaDatos[4], listaDatos[5], listaDatos[9], listaDatos[11]]
    sheet.append(nuevaFila)
    
def guardarExcelMarbete():
    book.save('files/Pruebas_Excel.xlsx')
    
def cerrarExcelMarbete():
    book.close()