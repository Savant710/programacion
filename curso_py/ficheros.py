'''Los ficheros son un objeto que te permiten interactuar
con el sistema de entrada y de salida para escribir
datos en el disco
open funcion basica de acceso a un fichero
el acceso de datos se puede realizar por:
read: lee un numero determinado de bytes
seek: de encarga de posiciona el lector en el byte indicado 
tell: devuelve ;a posicion que se esta leyendo en la actualidad
del fichero
close: cierra el fichero
'''
f = open('aritmeticas.py','r')
f.tell()
f.read(1)
f.read(3)
f.tell()
f.seek(2)
f.tell()
f.read(4)
f.close()
'''Metodo (readlines())'''
f = open('conjuntos.py','r')
lineas = f.readlines()
print(lineas[5])
print(lineas[:])
f.close()
#leer todo el fichero linea a linea
print("LEER TODO EL FICHERO LINEA A LINEA")
for line in open('conjuntos.py','r'):
    print(line)
'''Recorre las lieneas de un fichero origen y las copia
en el de destino'''
fwrite = open('copia_conjun.py','w')
for line in open('conjuntos.py','r'):
    fwrite.write(line)
fwrite.close()



