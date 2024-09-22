import openpyxl

def editarExcel(marbete, listaDatos):
    book = openpyxl.load_workbook('files/WMSOK.xlsx')

    sheet = book['registroArticulos']
    print(f'Marbete: {marbete}\n')
    nuevaColumna = (listaDatos[0], listaDatos[4],'' ,listaDatos[3], listaDatos[3], )
    # sheet.cell(row=13, column=1, value = 'HG40C1')
    # new_row = (1,'The Legend of Zelda',1986,'Action','Nintendo',3.74,0.93,1.69,0.14,6.51,6.5)

    # sheet.append(new_row)

    # book.save('files/WMSOK.xlsx')