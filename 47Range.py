from os import system

system('cls')

for numero in range(20, 31 ,2):
    print(numero)

#! 48 enumerate

lista = ['a', 'b', 'c' ]

for indice, item in enumerate(lista):
    print(item)
    print(indice)
    print(indice, item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[0][1])

#! 49 ZIP

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

paises_capitales = list(zip(paises,capitales))

print(paises_capitales)

for pais_capital in paises_capitales:
    print(f'La capital de {pais_capital[0]} es {pais_capital[1]}')

#! 50 Min y Max

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

print(f'El menor es {min(lista_numeros)} y el mayor {max(lista_numeros)}')

dic = {'C1':45, 'C2':11}

print(min(dic.values()))

print(min(dic))

#! 51 Random 

from random import randint

aleatorio = randint(1,20)
print(f'Aleatorio: {aleatorio}')

from random import *

colores = ['azul', 'rojo', 'verde', 'amarillo']

aleatorio = choice(colores)

print(f'Color seleccionado: {aleatorio}')

#! 52 Compresion
pies = [10, 20, 30, 40, 50]

metros = [p * 3.281 for p in pies]

print(metros)





