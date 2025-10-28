# EJERCICIO 2: CALCULADORA DE DESCUENTOS
# Una tienda ofrece descuentos según el monto de compra:
# - $0-$100: 0% descuento
# - $101-$500: 10% descuento
# - $501-$1000: 20% descuento
# - Más de $1000: 30% descuento

# Se debe de imprimir:
# Descuento Aplicado
# Monto del descuento
# Total a pagar

# monto = float(input('Ingrese el monto de la compra: $'))

# if monto <= 100:
#     descuento = 0
# elif monto <= 500:
#     descuento = 10
# elif monto <= 1000:
#     descuento = 20
# else:
#     descuento = 30

# monto_descuento = monto * (descuento/100)
# total_pagar = monto - monto_descuento

# print(f'Descuento Aplicado: {descuento}%')
# print(f'Monto del descuento: ${monto_descuento:.2f}') #el :.2f significa que vamos a redondear a DOS decimales
# print(f'Total a pagar: ${total_pagar:.2f}')


# EJERCICIO 3: VERIFICADOR DE TRIÁNGULOS
# Pide al usuario tres lados y determina:
# - Si forman un triángulo (la suma de dos lados debe ser mayor al tercero)
# - El tipo de triángulo: equilátero, isósceles o escaleno
# """

lado1 = float(input('Ingrese el primer lado: '))
lado2 = float(input('Ingrese el segundo lado: '))
lado3 = float(input('Ingrese el tercer lado: '))

#Verificar si es un triangulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Los lados si forman un triangulo')
    #Determinar el tipo de triangulo

    if lado1 == lado2 == lado3:
        tipo = 'Equilatero'
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        tipo = "Isosceles"
    else:
        tipo = "Escaleno"

    print(f'El triangulos es de tipo {tipo}')
else:
    print('Los lados suministrados no forman un triangulo')