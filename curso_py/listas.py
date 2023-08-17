lenguajes = ["Python", "Ruby","Php","Javascript", "Java"]
print(lenguajes)
#accede a un elemento en particular
print(lenguajes[0])
# Cambiar de elementos en una lista
lenguajes[1] = "Go"
print(lenguajes)
print(lenguajes[-1])
# Seleccipnar rangos de elementos
print(lenguajes[:3]) # es importante recordar que el el,emto final
# no se incluye
print(lenguajes[1:3])
#Metodos
#INSERTAR un elemento en ua psoicion en especifica
lenguajes.insert(3,"CSS")
print (lenguajes)
#insertat un nuevo elemento en la posicion entre javascript y java
#No olvides de recordar que tu lista ha cambiado
#considera aspectos de posicion para seguir agregando
#conforme tu lista cambie
lenguajes.insert(5,"C++")
print(lenguajes)
lenguajes.remove("Go")
print(lenguajes)
print("Php" in lenguajes)
# Se puede eliminar los elementos de una lista usando
#Clear
#lenguajes.clear()

#Accede al numero de elementos en la variable
print(len(lenguajes))

print(lenguajes)
#lenguajes.append(['Golab', 'HTML','SCRIPT'])
#print(lenguajes)
lenguajes.extend(['Golab', 'HTML','SCRIPT'])
print(lenguajes)
lenguajes.remove('SCRIPT')
print(lenguajes)
lenguajes1 = ['hola', 1, 'Jan']
print(lenguajes + lenguajes1)
print(lenguajes*2)
#remueve a la variable de acuerdo su indice
lenguajes.pop(0)
print(lenguajes)

my_new_lenguajes = lenguajes.copy()
print(my_new_lenguajes)
#reverse voltea el orden de mi lista
my_new_lenguajes.reverse()
print(my_new_lenguajes)
#sort nos sirve para ordenar la lista de una forma en especifico
my_new_lenguajes.sort()
print(my_new_lenguajes)



