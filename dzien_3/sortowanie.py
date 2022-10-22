import random

lista = [9,1,6,8,4,3,2,0]
for i in range(len(lista)):
    i_min_wartosc = i
    for i_ogona in range(i_min_wartosc, len(lista)):
        if lista[i_ogona] < lista[i_min_wartosc]:
            i_min_wartosc = i_ogona
            






