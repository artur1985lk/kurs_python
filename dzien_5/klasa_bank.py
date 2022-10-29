class Bank:
    # stan = 0
    def __init__(self):
        self.stan = 0

    def zwieszczanie_salda(self, wartosc):
        self.stan += wartosc
        return self.stan

    def zmiejszenia_salda(self, wartosc):
        self.wartosc = wartosc
        self.stan -= self.wartosc
        return self.stan

    def wartosc(self):
        print(self.stan)


konto_1 = Bank()
konto_1.zwieszczanie_salda(100)
konto_1.zwieszczanie_salda(80)
konto_1.wartosc()
konto_2 = Bank()
konto_2.wartosc()
