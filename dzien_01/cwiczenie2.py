waga = input("Podaj wagę ")
wzrost = input("Podaj wzrost w cm ")
result = round(int(waga) / ((int(wzrost) * int(wzrost) / 10000)), 2)
print(f"twoje bmi: {result}")