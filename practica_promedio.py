#Se requiere un programa que reciba el nombre del estudiante y le pregunte por las notas de los tres examenes parciales, se requiere:
#1. Calucle el promedio
#2. Determinar cual fue la nota mas alta y cual fue la mas baja
#3. El curso se aprueba con un prodio mayor a 75, por lo que debe de indicar si aprobo o no el curso.
#4. Imprimir todos los resultados
#Nota: el ejercicio se debe realizar con lo que se ha visto en la clase de hoy

nombre_estudiante = ''
nota_1 = 0
nota_2 = 0
nota_3 = 0
notas = []
condicion = "reprobado"

nombre_estudiante = input('Por favor ingrese su nombre: ')
nota_1 = float(input('Por favor ingrese la nota del examen #1: '))
notas.append(nota_1)
nota_2 = float(input('Por favor ingrese la nota del examen #2: '))
notas.append(nota_2)
nota_3 = float(input('Por favor ingrese la nota del examen #3: '))
notas.append(nota_3)

notas.sort()

nota_menor = notas[0]
nota_mayor = notas[2]

promedio = (notas[0]+notas[1]+notas[2])/ len(notas)
if promedio >= 75:
    condicion = 'Aprobado'



print('\n')
print('*'*12)
print(nombre_estudiante)
print(f'Examen 1: {nota_1}')
print(f'Examen 2: {nota_2}')
print(f'Examen 3: {nota_3}')
print(f'La nota menor fue de: {nota_menor} \n La nota mayor fue de: {nota_mayor}')
print(f'El promedio del curso es de: {promedio} \n {condicion} el curso')