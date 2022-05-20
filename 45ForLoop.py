from os import system

system('cls')

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c', 'clave4':'d' }

for item in dic.items():
    print(item)

for a,b in dic.items():
    print(a, b)

for item in dic.values():
    print(item)

for a,b in dic.items():
    print(item)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for item in alumnos_clase:
    print(f'Hola {item}')

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero  in lista_numeros:
    suma_numeros = suma_numeros + numero
print(f'El total es {suma_numeros}')

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0 
suma_impares = 0
for numero in lista_numeros:
    if(numero%2 == 0):
        suma_pares = suma_pares + numero
    if(numero%2 == 1):
        suma_impares = suma_impares + numero
print(f'El total de la suma de numeros pares es {suma_pares}')
print(f'El total de la suma de numeros impares es {suma_impares}')


    

