class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = width * height

    @property
    # moved the logic for returning area to a separate method
    def area(self):
        return self._area
    @staticmethod


object = Rectangle(10, 20)

print(object.area)