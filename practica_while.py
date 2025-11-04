# Imprimir las potencias de 2 (2, 4, 8, 16, etc.) mientras el resultado sea menor o igual a 500.

# potencia = 2

# while potencia <= 500:
#     print(potencia)
#     potencia = potencia * 2

# print('El siguiente resultado excede el limite de 500')


# palabra = 'dinosaurio'
# print(len(palabra))

#Utilizando el ciclo while, hagan un programa que pida una palabra al azar, luego que pida el buscar una letra de esa palabra, y que nos diga cuantas veces aparece

palabra = input("Por favor ingrese una palabra: ")
letra = input('Por favor ingrese la letra que desea buscar: ')


contador = 0
posicion = 0


while posicion < len(palabra):
    if palabra[posicion] == letra:
        contador += 1

    posicion += 1

print(f'La letra "{letra}" aparece {contador} veces en la palabra "{palabra}"')