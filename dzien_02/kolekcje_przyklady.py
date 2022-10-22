# # napis = "Ala ma kota"
# # print(len(napis))
# # print("A" in napis)
# # print(napis.lower().count("a"))
# # print(napis.index("A"))
# # print(napis[0])
# # napis = list(napis)
# #
# # t = (1, 2, 3, "a")
# # x = (6, 7)
# # print(*t, sep='')
# # print(str(t))
# #
# # a = [3,2,5]
# # c = a
# #
# # b = a.
# # b.append(6)
# # print(a, b, c)
#
# a = (1, 2, 2.000000000000000000000000001, 2)
# print(id(a[1]))
# print(id(a[2]))
# print(id(a[3]))
# print(a.count(2))
#
#
# # b =list(a)
# # b.append(5)
# # print(a, tuple(b))
#
# dane = (0,1,2,3,4,5,6,7,8,9)
# print(dane[1])
# print(dane[-2])
# print(dane[3:8])
# print(dane[::3])
# print(dane[::-1])
# dane = "abcdefghijk"
# print(dane[1])
# print(dane[-2])
# print(dane[3:8])
# print(dane[::3])
# print(dane[::-1])
# print()
#
# # Utwórrz liste 10 elementowa
# #
# # dołącz element do listy
# # wsadz nowy element przed 3 indexem
# # zmien wartosc na indeksie 5
# # zrzuć ostatnią wartość (pop)
# new = ["a", 1, 2 , 3 , 4 , 5, 6 , 7, 8, 9]
# new.append("a")
# print(new)
# new.insert(2, "a")
# print(new)
# new[4] = "n"
# print(new)
# new.pop(-1)
# print(new)

dane = []

while True:
    liczba = input("Podaj liczbę: ")
    if liczba == "k":
        break
    dane.append(int(liczba))

print("Srednia: ", sum(dane) / len(dane))
print("min", min(dane))
print("max", max(dane))
count_min = 0
count_plus = 0
for i in dane:
    if i < 0:
        count_min += 1
for i in dane:
    if i > 0:
        count_plus += 1
print("liczby ujemne: ", count_min)
print("liczby dodatnia: ", count_plus)
x = [a for a in dane if a < 0]
print(len(x))




# >>> x = [1, 2, 3, 4, 5]
# >>> y = [2*a for a in x if a % 2 == 1]

# x = lambda a, b : a * b
# print(x(5, 6))



