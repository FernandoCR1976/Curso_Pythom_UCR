# Reglas para años bisiestos:

# Un año es bisiesto si es divisible entre 4

# EXCEPCIÓN: No es bisiesto si es divisible entre 100

# EXCEPCIÓN DE LA EXCEPCIÓN: Sí es bisiesto si es divisible entre 400


print('DETERMINADOR DE ANIO BISIESTO')
print('='*40)
print('\n'+ '-'*30)
year = int(input('Ingrese un annio: '))

if year % 4 == 0:
    print(f'{year} es divisible entre 4')
    if year % 100 == 0:
        print(f'{year} es divisible entre 100')
        if year % 400 == 0:
            print(f'{year} es divisible entre 400')
            print(f'{year} ES BISIESTO')
        else:
            print(f'{year} NO es divisible entre 400')
            print(f'{year} NO ES BISIESTO')
    else:
        print(f'{year} NO es divisible entre 100')
        print(f'{year} ES BISIESTO')
else:
    print(f'{year} No es divisible entre 4')
    print(f'{year} NO ES BISIESTO')
print('\n'+ '-'*30)
print('Analisis Resumido')
print('\n'+ '-'*30)
print('\n'+ '-'*30)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} ES BISIESTO')
else:
    print(f'{year} NO ES BISIESTO')