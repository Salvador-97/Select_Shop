import json

with open("../files/marbetesNumeros.json") as archivoJSON:
    numeros = json.load(archivoJSON)
print(numeros)
