# import time
#
# counter = 0
# while True:
#     counter += 1
#     print("hallo word")
#     time.sleep(1)
#     if counter < 7:
#         continue
#     else:
#         break
# else:
#     print("i tak zrobiłem")


# import time
#
# counter = 0
# while counter < 100:
#     counter += 1
#     print(counter)
#     time.sleep(0.1)

# import time
#
# counter = "ddddd"
# while counter.count(1,3):
#
#     print(counter)
#     time.sleep(0.1)

# i = iter(range(10))
# while next(i):
#     print("one")
#
# suma = 0
# ilosc = 0
# najmiejsz = None
# najwieksza = None
# while True:
#     x = input("podaj liczbę: ")
#     if x == "k":
#         break
#     x = int(x)
#     if najwieksza is None or x > najwieksza:
#         najwieksza = x
#     if najmiejsz is None or x > najmiejsz:
#         najmiejsz = x
#     suma += x
#     ilosc += 1
#
# print("Srednia wynosi:", suma / ilosc)
# print("Min", najmiejsz)
# print("Max", najwieksza)



lista = []
while True:
    x = input("podaj liczbę: ")
    if x == "k":
        break
    lista.append(int(x))

print(lista)
print("średnia", sum(lista) / len(lista))
print("Min",min(lista))
print("Max", max(lista))



