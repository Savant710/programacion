# separa de esta lista a una nueva los animales que tengan 7 letras
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new=[]
i=0
for animales in Animals:
    #print(animales)
    a = Animals[i]
    if (len(animales) == 7):
        #print(len(animales),"Este animal tiene 7 letras entra a la nueva lista")
        new.append(a)
    #else:
        #print(len(animales), "No tiene 7 letras no entra")
    i+= 1
print(new)

print('Bucle While')
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
New = []
s=0
while s<len(Animals):
    j=Animals[s]
    if(len(j)==7):
        print(j,f"Este animal tiene {len(j)} letras entra a mi nueva lista")
        New.append(j)
    else:
         print(j,f"Este animal tiene {len(j)} letras no entra a mi nueva lista")
    s=s+1
print(New)
