class Car():
    counter = 0
    def __init__(self, brand):
        self.brand = brand
        Car.counter += 1
    def drive(self):
        print(f"samochod {self.brand} jedzie")



c = Car("fiat")
c.drive()
Car.drive(c)
print(Car.counter)
c = Car("BMW")
print(Car.counter)