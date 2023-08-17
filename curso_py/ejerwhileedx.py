PlayListRatings = [10, 9.5, 10, 8, 7.5, 7.5, 10, 10]
i = 0
rating = PlayListRatings[0]
while (i < len(PlayListRatings) and rating >=6):
    print(rating)
    i += 1
    # Aqui se usa un if para evitar que salga error al imprimir nuevamente
    #el valor de rating
    #ya que en este caso PlayListRatings[8] toma el valor de 8
    # y la lista solo tiene [0 a 7] valores 
    if i != len(PlayListRatings) :
        rating = PlayListRatings[i]
print("fin del while")