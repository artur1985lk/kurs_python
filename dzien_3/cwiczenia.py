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


liczby_wpisane = []
while True:
    l = input("Podaj liczbę: ")
    if l == " ":
        break
    else:
        liczby_wpisane.append(int(l))
liczby_parzyste = set(range(0, 100, 2))

print("Liczb parzystych jest: ", len(set(liczby_wpisane) & liczby_parzyste))


print("Oto te liczby: ", (set(range(0,100)) & set(liczby_wpisane)) & liczby_parzyste)

# d = lambda x: print([i ** 3 for i in x])

lista = {x for x in range(100) if x % 3 == 0}
print(lista)
print(x for x in range(100) if x % 3 == 0)