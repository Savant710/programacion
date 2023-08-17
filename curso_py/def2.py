def dome(dm, sty='*', spacing=(7)):
    large = spacing + len(dm)
    estilolin = sty * large
    print(estilolin)
    print(f'{dm:^{large}}')
    print(estilolin)

dome("te amo")
dome("te nesecito",spacing=17)
dome("te extraño",spacing=17,sty=':')
dome("Ya vuelve" ,";",8)