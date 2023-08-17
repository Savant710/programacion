def saludo(escribe_algo):
    largo = 10 + len(escribe_algo)
    estiloline = ':*' * largo
    print(estiloline)
    print(f'{escribe_algo:^{largo}}')
    print(estiloline)

saludo('Hola')
fotos = "Hoy es un buen dia para que me mandes fotos"
saludo(fotos)
def brillo(b):
   lon = 27
   estil = ":" * lon
   print(estil)
   print(f'{b:^{lon}}')
   print(estil)
brillo("YA SE PROGRAMAR")