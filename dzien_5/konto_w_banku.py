def konto():
    return {"stan": 0}


def zwieszczanie(konto, wartosc):
    konto['stan'] += wartosc
    return konto['stan']


def zmiejszenie(konto, wartosc):
    konto['stan'] -= wartosc
    return konto['stan']


konto_1 = konto()
print(konto_1)
zmiejszenie(konto_1, 100)
zwieszczanie(konto_1,80)
print(konto_1)
