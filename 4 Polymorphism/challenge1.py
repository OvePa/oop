class Shape:
    def __init__(self):
        self.name = "Shape"

    def getName(self):
        return self.name


class XShape(Shape):
    # initializer
    def __init__(self, name):
        super().__init__()
        self.xsname = name

    def getName(self):  # overriden method
        return super().getName() + "," + self.xsname


if __name__ == "__main__":
    rectangle = XShape("Rectangle")
    print(rectangle.getName())
    circle = XShape("Circle")
    print(circle.getName())
    triangle = XShape("Triangle")
    print(triangle.getName())
