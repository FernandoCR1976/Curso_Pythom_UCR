# datos primitivos

entero = 10
flotante = 3.14
cadena = 'Palabra'
booleanos = True


#Datos NO Primitivos
#1. listas, arreglos o arrays
lista = [1,2,3,4]
lista1 = [1.5,5.8,3.9]
lista2 = ['hola', 'lista', 'tomate', 'gallina']
lista3 = [True,True,False]
lista4 = [1,True,'palabra',3.14,[1,2,3]]

#2. TUPLA
tupla = (1,2,3)

#3. Diccionario
diccionario = {"Nombre": "Luis Fernando", 'edad': 49, 'Casado': True}

#4. Conjuntos
conjuntos = {1,2,3}

#==================================================
#LISTAS
lista = [1,2,3,4]

lista1 = [1.5,5.8,3.9]

lista2 = ['hola', 'lista', 'tomate', 'gallina']

lista3 = [True,True,False]
lista4 = [1,True,'palabra',3.14,[1,2,3]]

#print(lista)

#Necesito visualizar solamente el ultimo elemento de lista2
#print(lista2[3])

#Agregando elementos a una lista
estudiantes = ['Hugo', 'Paco', 'Luis']
#necesitamos agregar a Daysi a lista de alumnos
#print(estudiantes)
estudiantes.append('Daysi') #append agrega un elemento al final de la lista
#print(estudiantes)

#Necesitamos agregar a Donald en la segunda posicion de la lista 

estudiantes.insert(1,'Donald')
# print(estudiantes)

#Necesitamos agregar a Lucas en la ultima posicion de la lista, pero solamente podemos usar insert...por cierto, no sabemos el tamanno de la lista...

print(len(estudiantes))
estudiantes.insert(len(estudiantes),'Lucas')
# print(estudiantes)

#Quiero eliminar a Daysi de la lista estudiantes

estudiantes.remove('Daysi')
#print(estudiantes)

eliminados = estudiantes.pop(4)
# print(estudiantes)
# print(eliminados)

#Me piden ordenar la lista en orden ascendente

estudiantes.sort()
#print(estudiantes)

#Me piden ordenar la lista en orden descendente

estudiantes.reverse()
#print(estudiantes)

#Practica
#Cree una lista de compras de 6 elementos, agregue 2 mas, ordenelos alfabeticamente. Imprima casa uno de los pasos con print  f'

compras = ['leche','pan','arroz','zanahoria','jalea','mostaza']
print(f'La lista de compras actual contiene {compras}')
compras.append('cebollas')
print(f'La lista de compras ahora contiene {compras}')
compras.append('frijoles')
print(f'La lista de compras ahora contiene {compras}')
compras.sort()
print(f'La lista de compras contiene {compras}')