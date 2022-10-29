class Samochod():

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return f'Nazwa samochodu: {self.nazwa}'

my_car = Samochod('Fiat')
print(my_car)