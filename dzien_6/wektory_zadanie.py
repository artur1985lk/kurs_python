"""
Zaimplementuj klasę `Vector` dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinny
mieć możliwość dodawania, odejmowania, mnożenia (przez inny
wektor i przez liczbę), porównywania (po długości) oraz powinny
posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
"""


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x} {self.y})"

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        self.scalar = scalar
        return Vector(self.x * self.scalar, self.y * self.scalar)

    def __eq__(self, other):
        return Vector(self.x == other.x, self.y == other.y)

    # def __gt__(self, other):
    #     return self.__class__(self.x > other.x, self.y > other.y)
    #
    # def __ge__(self, other):
    #     return self.__class__(self.x >= other.x, self.y >= other.y)
    #
    # def __le__(self, other):
    #     return self.__class__(self.x < other.x, self.y < other.y)
    #
    # def __lt__(self, other):
    #     return self.__class__(self.x <= other.x, self.y <= other.y)


# vector_1 = Vector(x=1, y=2)
# vector_2 = Vector(x=1, y=2)
# print(vector_1.__mul__(3))
# vector_3 = vector_1 + vector_2
# print(vector_1 == vector_2)
# vector_3 = vector_1 + vector_2


class Test_Vector():

    def test_init(self):
        v = Vector(x=1, y=2)
        assert str(v) == "Vector(1 2)"

    def test_equality(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        v3 = Vector(2, 3)

        # assert v1 == v2
        # assert v2 == v3

    def test_match(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        assert v1 + v2 == "Vector(3 5)"
        # v = Vector(3,5)
        # assert v * 5 == 15
