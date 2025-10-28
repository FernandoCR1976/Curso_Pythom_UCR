#Programa para calcular el IMC y clasificarlo

#IMC se define peso en kg dividido entre la altura en metros elevado al cuadrado

#Menor a 18.5 peso inferior al normal
#18.5 a 24.9 peso normal
#de 25 a 29.9 peso superior al normal
# mayor a 30 Obesidad

peso = float(input('Por favor ingrese su peso en kilogramos: '))
altura = float(input('por favor ingrese su altura en metros: '))

imc = peso / (altura ** 2)

# if (imc < 18.5):
#     print(f'Su IMC es de {imc} y su condicion es de un peso inferior al normal')
# else:
#     if (imc < 25):
#         print(f'Su IMC es de {imc} y su condicion es de peso normal')
#     else:
#         if (imc < 30):
#             print (f'Su IMC es de {imc} y su condicion es de peso superior al normal')
#         else:
#             print(f'Su IMC es de {imc} y su condicion es de obesidad')

if (imc < 18.5):
    condicion = 'peso inferior al normal'
else:
    if (imc < 25):
        condicion = 'de peso normal'
    else:
        if (imc < 30):
            condicion = 'peso superior al normal'
        else:
            condicion =  'obesidad'

print(f'su IMC es de {imc}, y su condicion es de {condicion}')

if (imc < 18.5):
    condicion = 'peso inferior al normal'
elif (imc < 25):
    condicion = 'de peso normal'
elif (imc < 30):
    condicion = 'peso superior al normal'
else:
    condicion =  'obesidad'

print(f'su IMC es de {imc}, y su condicion es de {condicion}')
