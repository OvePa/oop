"""
Static methods
Static methods are methods that are usually limited to class only and not their
objects. They have no direct relation to class variables or instance variables.
They are used as utility functions inside the class or when we do not want the
inherited classes to modify a method definition.

Static methods can be accessed using the class name or the object name.

Syntax
To declare a method as a static method, we use the decorator < @staticmethod >.
It does not use a reference to the object or class, so we do not have to use
< self < or < cls >. We can pass as many arguments as we want and use this method to
perform any function without interfering with the instance or class variables.
"""


class Player:
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def demo():
        print("i'm a static method.")


class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


if __name__ == "__main__":
    # Access to static methond
    p1 = Player("lol")
    p1.demo()
    Player.demo()
    print("*" * 20)
    # Do not change anything, just give a result
    weight = 75
    height = 1.8
    print("BMI:", BodyInfo.bmi(weight, height))


"""
Static methods do not know anything about the state of the class, i.e., 
they cannot modify class attributes. The purpose of a static method is to use 
its parameters and produce a useful result.
"""
