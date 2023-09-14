class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        area = self.__width * self.__length
        return area

    def perimeter(self):
        perimeter = 2 * (self.__width + self.__length)
        return perimeter


if __name__ == "__main__":
    r = Rectangle(4, 5)
    print("Area", (r.area()))
    print("Perimeter:", r.perimeter())
