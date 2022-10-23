"""
Jaką operacje chcesz wykonać:
1 - dodawanie
2 - odjmowanie
3 - mnożenie
4 - dzielenie
>>> kalkulator(4,4,4)
1.0

"""



def kalkulator(x, y, znak: int):
    if znak == 1:
        return x + y
    elif znak == 2:
        return x - y
    elif znak == 3:
        return x * y
    elif znak == 4:

        return x / y


try:
    operacja = int(input("""
    Jaką operacje chcesz wykonać:
    1 - dodawanie
    2 - odjmowanie
    3 - mnożenie
    4 - dzielenie

    """))
    x = int(input("Podaj liczbę pierwszą: "))
    y = int(input("Podaj liczbę drugą: "))
    print("Wynik to ",round(kalkulator(x,y,operacja),4))

except ZeroDivisionError:
    print("Nie dziel przez zero")
