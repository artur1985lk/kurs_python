# plansza 10x10
import random

DEBUG = True

skarb = [random.randrange(1, 11), random.randrange(1, 11)]
pozycja_gracza = [random.randrange(1, 11), random.randrange(1, 11)]

odleglosc_poczatkowa = abs(skarb[0] + pozycja_gracza[0]) + abs(skarb[1] + pozycja_gracza[1])
while True:
    odleglosc = abs(skarb[0] + pozycja_gracza[0]) + abs(skarb[1] + pozycja_gracza[1])
    if DEBUG:
        print("pozycja skarbu", skarb)
        #print("odległość do skarbu", odleglosc_poczatkowa)
        #print("odległość", odleglosc)
    print("pozycja gracza", pozycja_gracza)
    print()
    ruch = input("Wykonaj ruch: w,s,a,d ")
    if ruch == "w":
        pozycja_gracza[1] = pozycja_gracza[1] + 1
    if ruch == "s":
        pozycja_gracza[1] = pozycja_gracza[1] - 1

    if ruch == "a":
        pozycja_gracza[0] = pozycja_gracza[0] - 1
    if ruch == "d":
        pozycja_gracza[0] = pozycja_gracza[0] + 1

    if pozycja_gracza[0] not in range(1, 11) or pozycja_gracza[1] not in range(1, 11):
        print("jesteś poza planszą")
        break

    if pozycja_gracza == skarb:
        print("znalazłęś skarb")
        break

    # 13 -11   13 - 12

# while True:
