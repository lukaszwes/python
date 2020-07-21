class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def count_surface_area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a,a)

class Cube():
    def __init__(self, figure: Square):
        self.figure = figure
    def count_surface_area(self):
        return self.figure.count_surface_area() * 6
    def count_volume(self):
        return self.figure.count_surface_area() * self.figure.a

class Cuboid:
    def __init__(self, base: Rectangle, high):
        self.base = base
        self.high = high
    def count_surface_area(self):
        return 2 * (self.base.count_surface_area() + self.base.a * self.high + self.base.b * self.high)
    def count_volume(self):
        return self.base.count_surface_area() * self.high





print(Rectangle(2,3).count_surface_area())

print(Square(3).count_surface_area())

print(Cube(Square(3)).count_surface_area())
print(Cube(Square(3)).count_volume())

print(Cuboid(Rectangle(2,3),4).count_volume())