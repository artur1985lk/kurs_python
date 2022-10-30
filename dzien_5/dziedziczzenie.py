import datetime


class User:
    def __init__(self, imie, dataurodzenia):
        self.imie = imie
        self.dataurodzenia = dataurodzenia
        self.inicjal = imie[0]
        self.rokurodzenia = dataurodzenia[0:4]
    def __repr__(self):
        pass

    def drukuj(self):
        print(self.imie, self.dataurodzenia)
    def wiek(self):
        dzis = datetime.datetime.now()
        yyyy = self.dataurodzenia[0:4]
        wiek = int(dzis.year) - int(yyyy)
        return wiek

user = User("Tomek", "19991204")
# user.drukuj()
# print(user.inicjal)
# print(user.dataurodzenia)
print(user.wiek())

class Administrator(User):
    def dostep(selfself):
        return True

adminstrator = Administrator("Adam", "20001203")
print(adminstrator.wiek())

class Wlasciciel(Administrator):
    pass

class Magazyn():
    pass
class Zatowarowanie(Magazyn):
    pass

class RozchodTowaru(Magazyn):
    pass

class Sklep(Zatowarowanie, RozchodTowaru, Magazyn):
    pass




class Trojkat():
    def pole_t(self):
        pass
class Kolo():
    def pole_k(self):
        pass
class Kwadrat():
    def pole_kw(self):
        pass

class Figury(Trojkat, Kolo, Kwadrat):
    pass