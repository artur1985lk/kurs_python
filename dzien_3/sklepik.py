import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def obliczanie():
    print("dodaję do koszyka ")
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".", end='')
    time.sleep(0.1)
    print(".")


produkty = {"marchew": 3, "ziemniaki": 5, "cebula": 2, "buraki": 3}
print(bcolors.WARNING + """Witaj w warzywniaku.
Oferujemy:
  -marchew: 3 PLN / kg
  -ziemniaki: 5 PLN / kg
  -cebula: 2 PLN / kg
  -buraki: 3 PLN / kg

""" + bcolors.ENDC)


stan_magazynowy_kg = {"marchew": 5.0, "ziemniaki": 5.0, "cebula": 5.0, "buraki": 5.0}

kwota = 0
while True:
    co_robisz = input(bcolors.OKBLUE + "Co chcesz robić: \n  -zakupy \n  -dodawanie do magazynu\n"  + bcolors.ENDC)
    wybor_pentli = co_robisz
    while wybor_pentli == "dodawanie do magazynu":
        jaki = input("Podaj produkt który chcesz dodać lub wpisz 'exit' jeśli chcesz wyjść:\n")
        if jaki == "exit":
            break
        waga_do_dodania = float(input("Ile chcesz dodać\n"))
        stan_magazynowy_kg[jaki] += waga_do_dodania

    while wybor_pentli == "zakupy":
        nazwa = input("Co chcesz kupić: ")
        if nazwa == "exit":
            break
        waga = float(input("Ile kg: "))
        cena_za_jeden_produkt = produkty[nazwa] * waga
        if stan_magazynowy_kg[nazwa] >= waga:
            stan_magazynowy_kg[nazwa] -= waga
            kwota += cena_za_jeden_produkt
            obliczanie()
            print(f"Do zapłaty {kwota:5.2f} zł\n")
        else:
            print("Nie mamy tyle produktu na magazynie")
            print("jeśli chcesz zakończyć wpisz exit\n")






result = 0
print(f"Nalerzy się: {result}")