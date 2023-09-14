class Circle:
    # Insert your code here
    def __init__(self, radius=None):
        self.__radius = radius
        self.__pi = 3.14

    def setRadius(self, radius):
        self.__radius = radius

    def print_area(self):
        area = self.__pi * (self.__radius * self.__radius)
        return area


c = Circle(4)
print(c.print_area())
c.setRadius(3)
print(c.print_area())
