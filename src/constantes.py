CONSTANTES_CARACTERISTICAS = 'Siempre se escriben en mayusculas'
TMB_PUEDEN_SER_UN_NUM = 1234

import keyword
print(keyword.kwlist)

'''
Esta linea de codigo no es ejecutada
'''
x = 7
y = 3

z = x + y

#x%= y
divnorm = x/y
divent = x//y
print(z)
print(x)
print(divnorm)
print(divent)
'''Jerarquia de python () ,**, *, /, +, -'''
jer = 4 * 3 + 5
print(jer)
jer2 = 7 + 9 ** 2 /3
print(jer2)

hola = int(input("ingrese un numero "))
while hola != 7:
    hola = int(input("ingrese un numero "))
    if  6< hola < 8:
        print(f'este es mi numero favorito {hola}')
print('Estamos practicando mucho')


