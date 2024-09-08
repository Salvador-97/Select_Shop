import json

with open("files/marbetesNumeros.json") as archivoJSON:
    numeros = json.load(archivoJSON)
print(numeros)

filaKey = 'AM'

#10026

if filaKey in numeros:
    print(numeros[filaKey])
    numeros[filaKey] = numeros[filaKey] + 10
    with open("files/marbetesNumeros.json", "w") as archivoJSONedit:
        json.dump(numeros, archivoJSONedit)
    print(numeros[filaKey])
    
    # 10789