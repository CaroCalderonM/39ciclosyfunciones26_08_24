numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    
language = 'Python'

from collections.abc import Iterable #Aquí importamos el módulo Iterable, se debe usar collections.abc
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable)) #True (instance nos permite saber si un elemento es iterable)
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista:
    if numero == 5:
        break
    print(numero)
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encontrado = None
for numero in lista:
    if numero == 5:
        encontrado = numero
        break
    print(numero)
print("Encontrado: ", encontrado)

for i in range(10):
    print("**********")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(2, 6, 2):
    print(lista[i])
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista[2:5:2]:
    print("iterador", i)
    print(lista[i])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(2, 6):
    print(lista[i])

#Otro ejemplo
#REVISARLO POR QUÉ ME MARCA ERROR

#matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#for lista in matriz:
#    for numero in lista:
#    print(lista)

pokemones = [
    {"id": 1, "nombre": "Ditto", "habilidades": ["transformación", "copiar", "duplicar"]},
    {"id": 2, "nombre": "Charizard", "habilidades": ["transformación", "copiar", "duplicar"]},
    {"id": 3, "nombre": "Pikachu", "habilidades": ["transformación", "copiar", "duplicar"]},
]

#for pokemon in pokemones:
#    print("Nombre pokemón: ", pokemon["nombre"])
    
    
#    print("Habilidades: ")
#    print(pokemon["habilidades", habilidad])
#    for habilidad in pokemon["habilidades", habilidad]
#        print(habilidad)
#    print("******************************************")
    
#print(f"Habilidades ({len(pokemon["habilidades"])})")
    

#EJEMPLO DE POKEMONES (Realizado por el profesor)

pokemones = [
    {"id": 1, "nombre": "Ditto", "habilidades": ["transformación", "copiar", "duplicar"]},
    {"id": 2, "nombre": "Charizard", "habilidades": ["escupir fuego", "volar"]},
    {"id": 3, "nombre": "Pikachu", "habilidades": ["Ataque electrico", "Saltar", "correr"]},
]
 
for pokemon in pokemones:
    print("Nombre pokémon:", pokemon["nombre"])
    habilidades = pokemon["habilidades"]
    cant_habilidades = len(habilidades)
    print(f"Cantidad de habilidades: {cant_habilidades}")    
    for habilidad in habilidades:
        print(habilidad)
    print("*************************************")
    
    
nombre = "Carlos"

it = iter(nombre)

print((it))
print(next(it))  #Si me paso de la cantidad de caracteres que tiene el string, me arroja error.
print(next(it))  #En este caso es 6 porque tiene 6 letras
print(next(it))  # Revisar cómo considera los espacios de una frase u oración
print(next(it))
print(next(it))
print(next(it))


lista = [1, 2, 3, 4, 5, 6, 7]

it = iter(lista)
#probar aquí agregando un ciclo for
print(next(it))  #El next me podría servir para mostras las imágenes de un carrusel y volver al inicio cuando avanza desde la última
print(next(it))  #next es SECUENCIAL, va uno por uno.

#funciones generadoras
# Ejemplo: yield



