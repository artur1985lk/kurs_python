"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny policz
jako nadgodziny (z podwójną stawką godzinową).
Przykład użycia:
# >>> b = Biuro()
# >>> b.add_employee(employee)
# >>> b.explort("dane.csv")
imie;nazwisko;stawka;godziny
Jan;Kowalski,100.0,5
"""
import csv


class Biuro():
    def __init__(self, name, surname, rete_per_hour, time):
        self.rete_per_hour = rete_per_hour
        self.time = time
        self.surname = surname
        self.name = name
        self.columns = ["name", "surname", "rete per hour", "time"]

    def zapisywanie(self):

        dane = [self.name, self.name, self.rete_per_hour, self.time]

        with open("dane.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(self.columns)
            writer.writerow(dane)

    def odczytywanie(self):
        dane = [self.name, self.name, self.rete_per_hour, self.time]

        with open("dane.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'{", ".join(row)}')
                    line_count += 1
                else:
                    print(f'{row}')
                    line_count += 1
            print(f'Processed {line_count} lines.')


b = Biuro("Jan", "Kowalski", "100", "0,5")
b.odczytywanie()
c = Biuro("Pawel", "Kowalski", "100", "0,5")
c.zapisywanie()
Biuro.odczytywanie()
# class Employee():
#     def __init__(self, name, surname, rete_per_hour):
#         self.name = name
#         self.surname = surname
#         self.rete_per_hour = rete_per_hour
#         self.time = 0
#         self.salary = 0
#
#     def register_time(self, time):
#         self.time += time
#
#     def pay_salary(self):
#
#         if self.time <= 8.0:
#             self.salary = self.time * self.rete_per_hour
#             self.time = 0
#             return self.salary
#         else:
#             self.time = 0
#             self.salary = 8 * self.rete_per_hour + (self.rete_per_hour * 2 * (self.time - 8))
#             return self.salary
#
#
# employee = Employee('Jan', 'Nowak', 100.0)
# employee.register_time(5)
# print(employee.pay_salary())
# print(employee.pay_salary())
# employee.register_time(10)
# print(employee.pay_salary())
#
#
# def test_Employee_init():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert employee
#     assert employee.rete_per_hour == 100.0
#     employee.register_time(5)
#     assert employee.pay_salary() == 500
#     assert employee.pay_salary() == 0
#     employee.register_time(10)
#     assert employee.pay_salary() == 1200.0
