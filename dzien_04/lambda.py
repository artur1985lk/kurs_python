def second(x):
    return x[1]


y = lambda x: x[1]
lista = ["a5", "c0", "b1"]
print(sorted(lista, key=second))
print(sorted(lista, key=lambda x: x[1]))
print(sorted(lista, key=y))

xxx = lambda x, y: print(x + y)
xxx(1, 2)

data = [1, 2, 3, 4, 5, 6, 7]
start = lambda x: x > 3
stop = lambda x: x == 6

new = [i for i in data if i > 3]

*a, b, c = 1,2,3,4,5,6,7
print(a,b,c)
l = [1,2,3]
l1 = [5,6,7]
print(zip(l, l1))
