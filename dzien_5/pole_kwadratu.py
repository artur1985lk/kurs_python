import time


class Kwadrat():

    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        self.pole = pow(self.bok, 2)
        return self.pole

start = time.time()
kwadrat1 = Kwadrat(4)
print(kwadrat1.pole())
end = time.time()
print(end-start)
