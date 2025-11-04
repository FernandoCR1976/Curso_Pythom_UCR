# Ciclo While
# while (condicion a evaluar)
    #Bloque de codigo a repetir

    # cambiar la condicion para que finalice el bucle

# contador = 0

# while contador <= 5:
#     print(f' El valor actual es: {contador}')
#     contador = contador + 1

# cuenta_regresiva = 10

# while cuenta_regresiva >= 0:
#     print(f' El valor actual es: {cuenta_regresiva}')
#     cuenta_regresiva = cuenta_regresiva - 1

cnt_examenes = int(input('Ingrese cuantas notas va a evaluar: '))
notas = []
cnt_notas = 0 #este es mi contador
acumula_notas = 0

while cnt_notas < cnt_examenes :
    nota = float(input(f'Ingrese la nota del examen #{cnt_notas + 1}: '))
    acumula_notas = acumula_notas + nota
    notas.append(nota)
    cnt_notas = cnt_notas + 1

promedio = acumula_notas / cnt_notas
print(f'El promedio de las notas es {promedio}')
