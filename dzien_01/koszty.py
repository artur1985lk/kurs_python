while True:
    miasto_a = input("Podaj miasto startowe: ")
   
    try:
        miasto_b = input("Podaj miasto końcowe: ")
        dystans_a_do_b = int(input("Podaj dystans: "))
        cena_paliwa = float(input("Podaj cenę paliwa "))
        spalanie_na_100 = 8
        koszt_przejazdu_a_b = spalanie_na_100 * cena_paliwa * (dystans_a_do_b / 100)
        print(f"Kosty przejazdu z {miasto_a} do {miasto_b} to {koszt_przejazdu_a_b} zl")
        a = False
        break
    except:
        print()
        print("podaj prawidłowe dane")
        print()