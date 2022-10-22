
"""to jest funkcja która sprawdz czy podana liczba to liczba pierwsza"""
def czy_to_liczba_pierwsza(arg: int)-> bool:
    list = set(range(2,arg))
    if arg == 2:
        return True
    else:
        for i in list:
            if arg % i == 0:
                return False
    return True


liczba = int(input("Podaj liczbę: "))
if czy_to_liczba_pierwsza(liczba):
    print("To liczba pierwsza")
else:
    print("To nie jest liczba pierwsz")