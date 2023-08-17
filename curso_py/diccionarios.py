diccionario = {'nombre':'Mateo', 'edad':24, 'numfav': (7,24,27)}
tupla = (('nombre','Mateo'),('edad', 24),('numfav', (7,24,27)))
diccionario2 = dict(tupla)

a = diccionario['numfav']
print(a)

diccionario3 = {'libros': "Napoleon Hill", 'telefono':968493064}
print('nombre'in diccionario2)
 # la variable update nos srive para agregar un diccionario dentro del otro
 #y convertirlo en uno solo
diccionario.update(diccionario3)
print(diccionario)

del diccionario['telefono']
print(diccionario)
print('nombre' in diccionario)

