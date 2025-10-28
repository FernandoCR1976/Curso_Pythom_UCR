#Tipos de datos que hay en Python

#Existen dos grandes familias de datos, Primitivos y los No-Primitivos

#Datos primitivos
#Integer van a ser todos aquellos numeros que son enteros
#Float que son todos aquellos numeros que poseen decimales
#String que son las cadenas de texto que utilizan letras o simbolos
#Boolean True o False

#Datos NO Primitivos

#Arreglos
#Tuplas
#Diccionarios
#Datos creados por el desarrollador


# palabra = "Luis"
# print(palabra)
# print(type(palabra))
# oracion = 'Esto es una oracion'
# print(oracion)
# print(type(oracion))

# numero = 25
# otro_numero = 22.89

# print(type(numero))
# print(type(otro_numero))

# variable = None

# print(type(variable))

# variable = False
# print(type(variable))



# nombre = input('Por favor digite su nombre: ')

# print('Hola, ',nombre,', bienvenido al curso de Python 1')
# print(f'Hola {nombre}, bienvenido al curso de Python')

#Hacer una rutina que pida dos numeros y los sume

numero_1 = float(input('Ingrese el primer numero: '))
numero_2 = float(input("Ingrese el segundo numero: "))
resultado = numero_1 + numero_2
print(f'El resultado de la suma de los dos numeros es: {resultado}')
print(type(resultado))

cuadrado = numero_1 ** 2

print(cuadrado)
