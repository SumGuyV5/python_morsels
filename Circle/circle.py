import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return self.__repr__()

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value
        self.__diameter = value * 2
        self.__area = math.pi * value ** 2

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        raise AttributeError("Area cannot be set.")



if __name__ == '__main__':
    c = Circle(2)
    #c.diameter = -1
    print(c.radius)
    print(c.diameter)
    print(c.area)