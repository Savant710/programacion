'''EXISTEN DOS TIPOS DE CONJUNTOS
SETS MUTABLES Y FROZENSETS INMUTABLES
Longitud de un conjunto (len)
Pertenencia a un conjunto (in)
Union (union)
Interseccion(intersection)
Añadir elementos(add)
Eliminar un elemnto (remove)'''
conjunto1 = set([1,2,3,4])
conjunto2 = set([3,4])
conjunto1.remove(1)
conjunto2.add(5)
print(conjunto1)
print(conjunto2)

uniconjun = conjunto1.union(conjunto2)
interconjun = conjunto1.intersection(conjunto2)
print(uniconjun)
print(interconjun)
print(conjunto1, conjunto2)


