import openpyxl

def archivoEditable(ruta):
    global bookPath
    bookPath = ruta
    print(f'Funcion editExcel path: {bookPath}')

def ruta():
    return bookPath

def reiniciarContador():
    contador = 2

def editarExcel(listaDatos, contador):
    print(f'Archivo editExcel path: {bookPath}')
    # print(listaDatos)
    book = openpyxl.load_workbook(bookPath)

    sheet = book['entarimadoLote']
    # print(f'Marbete: {marbete}\n')
    # nuevaFila = (listaDatos[0], listaDatos[4],'' ,listaDatos[3], listaDatos[3])
    # print(f"Fila: {contador}")
    sheet.cell(row=contador, column=1, value=listaDatos[0])
    sheet.cell(row=contador, column=2, value=listaDatos[11])
    sheet.cell(row=contador, column=3, value=listaDatos[1])
    # sheet.cell(row=13, column=1, value = 'HG40C1')
    # new_row = (1,'The Legend of Zelda',1986,'Action','Nintendo',3.74,0.93,1.69,0.14,6.51,6.5)

    # sheet.append(nuevaFila)

    book.save(bookPath)
    
bookPath = ''