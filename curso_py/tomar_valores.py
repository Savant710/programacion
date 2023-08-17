
'''
Si quieres tomar valores de una lista usa for 
en este caso i toma los valores de la lista
'''
lista = [7, 'hola', 77, 'te', 777, 'amo']
for i in lista:
    print(i)


'''
Si quieres tener los valores de una lista y su indice usa for i,x in enumerate(lista)
donde i va a ser el indice y x los elementos de la lista
'''
lista = [7, 'hola', 77, 'te', 777, 'amo']
for i, x in  enumerate (lista):
    print(i,x)