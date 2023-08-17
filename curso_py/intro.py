# en python puedes utilizar 0b y escribir en binario
print(0b0001)
# si nesecitas en octal usa 0o
print(0o10)
# si nesecitas en hexadecimal0x
print(0x16)
# si nesecitas que una cadena de texto muestre comillas
#usa \para poder mostar en el texto
#tambien podemos utilizar \n para saltar la linea de un texto
#\t nos dara un salto de sangria
print("\"se bueno con los nerds, incluso puede que termines\ntrabajando para uno de ellos\"\t(Bill Gates)")
# cadenas entre comillas triples
nombre= "Mateo"
edad = 25
apellido = "Brito"
mis_datos = f'''nombre: {nombre}
edad: {edad}
apellido: {apellido}'''
print(mis_datos)
#tambien puedo escribir directamente
hola = '''Este es un mensaje para todos ustedes\nrecuerden tomar agua\n\tTe amo (Dome)'''
print(hola)
str1 = 'como'
str2 = 'estas'
str3 = '?'
unionstr = f'{str1}  {str2}  {str3}'
print(unionstr)
#para escribir un texto alineado se usa(:^10)
print(f'{str1:^10}')
#para escribir un texto alineado a la derecha se usa(:10)
print(f'{str1:>10}')
# si quieres agrgar algun caracter usa (:($)el caracter <10)
print(f'{str1:$<10}')
#centra tu string con un caracter de por medio usando (: (el caracter @) ^10)
print(f'{str1:@^10}')
#Transforma directamente a binario octal o hexadecimal
num=10
print(f'{num:b}')
print(f'{num:o}')
print(f'{num:x}')
