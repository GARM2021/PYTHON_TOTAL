from os import system

system('cls')

respuesta = 's'

while respuesta == 's':
    respuesta = input('Quieres seguir? (s/n)')
else:
    print('Gracias')

letra = " "
nombre = input("Tu Nombre: ")

for letra in nombre:
    if(letra != 'r'):
        print(letra)
    elif(letra == 'r'):
        break

for letra in nombre:
    if(letra != 'r'):
       continue
    elif(letra == 'r'):
         print(letra)


numero = 10
while numero > -1:
    print(numero)
    numero -= 1
