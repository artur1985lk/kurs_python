# def foo(a):
#     print(a)
#     if a == 100:
#         return a
#     return foo(a + 1)
# foo(1)

# def silnia(n):
#     if n == 0:
#         return 1
#     return  n * silnia(n - 1)
#
# print(silnia(5))

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return  n + fibo(n)

print(fibo(6))