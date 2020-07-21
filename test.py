import random
"""

class Car:
    def __init__(self):
        self.mass = random.randint(600, 1500)
        self.hp   = random.randint(90, 300)
        self.index = self.mass / self.hp
    def __str__(self):
        return ("Indeks camochodu wynosi " + str(self.index))

class CreateCars:
    def __init__(self, amountOfCars=2):
        self.cars = [Car() for _ in range (amountOfCars)]

    def getCars(self):
        return self.cars

    def __getitem__(self, key):
        return self.cars[key]


cars = CreateCars(2)

print(cars)

"""
class Prostokat:
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b
    def Pole(self):
        return self.bok_a * self.bok_b
    def __str__(self):
        return ("Pole figury {}x{} wynosi {}".format(self.bok_a, self.bok_b, self.Pole()))

class Figury:
    def __init__(self, figure_altitude):
        self.altitude = figure_altitude
        self.figury = [Prostokat(random.randint(1,10), random.randint(1,10)) for _ in range(self.altitude)]

        for figura in self.figury:
            print("Pole figury {}x{} wynosi {}".format(figura.bok_a, figura.bok_b, figura.Pole()))

    def __getitem__(self, key):
        # return self.figury[key]
        return ("Pole figury {}x{} wynosi {}".format(self.figury[key].bok_a, self.figury[key].bok_b, self.figury[key].Pole()))

    def __setitem__(self, key, value):
        self.figury[key].bok_a = value


baza = Figury(3)
print()
print(baza.figury[1])
baza[1] = 10
print(baza[1])





