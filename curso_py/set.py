my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {'Mateo', 'Brito', 24}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Savant')
print(my_other_set)
# un set no es una estructura ordenada
# ademas no tiene mas elementos repetidos
# tambien podemos eliminar con remove los elementos
my_other_set.remove('Mateo')
