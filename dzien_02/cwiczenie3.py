
# x = [1,2,3,4,5,6,7,8,9]
# szesciany = [i ** 3 for i in x]
# d = lambda x: print([i ** 3 for i in x])
# print(szesciany)
# szesciany2 = tuple(i ** 3 for i in x)
# print(szesciany2)

x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
print()
print("  ", *x, sep="   ")
print()
for i in x:
    print(i, end='  ')
    for j in y:
        x = i * j
        print(f"{x:3}", end=" ")
    print()