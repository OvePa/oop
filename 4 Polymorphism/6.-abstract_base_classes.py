"""
What are Abstract Base Classes?
Duck typing is useful as it simplifies the code and the user can implement the
functions without worrying about the data type. But this may not be the case
all the time. The user might not follow the instructions to implement the
necessary steps for duck typing. To cater to this issue, Python introduced the
concept of abstract base classes, or ABC.

Abstract base classes define a set of methods and properties that a class must
implement in order to be considered a duck-type instance of that class.

Why use abstract base classes?
Let’s see an example to understand why we should use abstract base
classes.
"""


class Shape:  # Shape is a child clas of ABC
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


shape = Shape()
square = Square(4)

"""
In the example above, you can see that an instance of Shape can be created even 
though an object from this class cannot stand on its own. The Square class, 
which is the child class of Shape, actually implements the methods area() and 
perimeter() of the Shape class. Shape class should provide a blueprint for its 
child classes to implement methods in it. To prevent the user from making a S
hape class object, we use abstract base classes.
"""
