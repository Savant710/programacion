lenguajes = ["Python", "Rubi","Php","Javascript", "Java"]
i = 0
# Se Utiliza la funcion len para tomar los valores de la 
#variable lenguaje
while i < len(lenguajes):
    print(lenguajes[i])
    i = i + 1
print(lenguajes)
# La mejor forma de acceder a los elementos de un listado
#for "cualquier letra o palabra" in tu_lista:
#for n in (tu_lista):
#accedera en orden a lso elementos de tu lista hasta terminar

for a in lenguajes:
    print(a)
mi_lista = [1, 2, 3, 4, 5, 6, 7]
for b in mi_lista:
    print(b)
#Otro ejemplo
tu_lista = ["Hola", "Que", "Hace", "?"]
for n in  tu_lista:
    print(n)
# Uso de break 
#break rompe el bucle cuando se cumple la codicion
coleccion = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for c in coleccion:
    if c == 8:
        break
    print(c)
# uso de continue
print("aqui comienza la parte de (continue)")
coleccion1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for d in coleccion1:
    if d % 2 !=0:
        continue
    print(d)


    
# en este caso continue permite seguir a la siguiente operacion
# por ejemplo el %1 es diferente entonces continua haciendo la operacion if
# el residuo de 2 es 0 entonces imprime 2

