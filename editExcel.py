import openpyxl

def archivoEditable(ruta):
    global bookPath
    bookPath = ruta
    print(f'Funcion editExcel path: {bookPath}')

def editarExcel(marbete, listaDatos):
    print(f'Archivo editExcel path: {bookPath}')
    print(f'Marbete: {marbete}')
    book = openpyxl.load_workbook(bookPath)

    sheet = book['registroArticulos']
    # print(f'Marbete: {marbete}\n')
    nuevaFila = (listaDatos[0], listaDatos[4],'' ,listaDatos[3], listaDatos[3])
    # sheet.cell(row=13, column=1, value = 'HG40C1')
    # new_row = (1,'The Legend of Zelda',1986,'Action','Nintendo',3.74,0.93,1.69,0.14,6.51,6.5)

    sheet.append(nuevaFila)

    book.save(bookPath)
    
bookPath = ''