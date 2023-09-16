"""
Syntax
To define an abstract base class, we use the abc module. The abstract base class
is inherited from the built-in ABC class. We have to use the decorator
@abstractmethod above the method that we want to declare as an abstract method.
"""
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


shape = Shape()
# this code will not compile since Shape has abstract methods without
# method definitions in it
