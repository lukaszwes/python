"""
    Stwórz trzy klasy:
    1) Rectangle - prostokąt
    2) Square - kwadrat
    3) Cube - sześcian

    a) Stwórz konstruktory (__init__)
    b) metody obliczające powierzchnię kwadratu, prostokąta, sześcianu
    c) metodę obliczającą objętość sześcianu

    Zastanów się jak możesz wykorzystać do tego dziedziczenie, aby nie powtarzać kodu
"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def count_surface_area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a,a)

class Cube(Square):
    def count_surface_area(self):
        return super().count_surface_area() *6
    def count_volume(self):
        return super().count_surface_area() * self.a


print(Rectangle(2,3).count_surface_area())

print(Square(3).count_surface_area())

print(Cube(3).count_surface_area())
print(Cube(3).count_volume())