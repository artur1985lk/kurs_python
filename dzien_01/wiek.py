#  test
while True:
    x = int(input("podaj liczbę: "))
    y = int(input("podaj liczbę: "))
    if x in range(0, 10) and y in range(0, 10):
        print("Lewy Dol")
    elif x in range(10, 90) and y in range(0, 10):
        print("Centrum Dol")
    elif x in range(90, 100) and y  in range(0, 10):
        print("Prawy Dol")
    elif x in range(0, 10) and y in range(11, 90):
        print("Lewy Centrum")
    elif x in range(10, 90) and y in range(11, 90):
        print("Centrum")
    elif x in range(90, 100) and y in range(11, 90):
        print("Prawe centru,")

    elif x in range(0, 10) and y in range(91, 100):
        print("Centrum gora")
    elif x in range(10, 90) and y in  range(91, 100):
        print("Centrum gora")
    elif x in range(91, 100) and y in range(91, 100):
        print("C gora")
    else:
        print("jesteś poza")
        break

    print()
    # znak = input()
    # znaki = ["-","+","/","*","**"]
    # if not(znak in znaki):
        # print("podałeś zły znak")
    # elif znak == "+":
        # print(x + y)
    # elif znak == "-":
        # print(x - y)
    # elif znak == "*":
        # print(x * y)
    # elif znak == "/":
        # print(x / y)
    # elif znak == "**":
        # print(x ** y)


