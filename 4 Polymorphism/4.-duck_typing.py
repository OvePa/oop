"""
Implementing Polymorphism Using Duck Typing

Duck typing is one of the most useful concepts in object-oriented programming
in Python. Using duck typing, we can implement polymorphism without using
inheritance.

-> What is duck typing?#
We say that if an object quacks like a duck, swims like a duck, eats like a
duck or in short, acts like a duck, that object is a duck.

-> Dynamic typing
Duck typing extends the concept of dynamic typing in Python.

Dynamic typing means that we can change the type of an object later in the code.

Due to the dynamic nature of Python, duck typing allows the user to use any
object that provides the required behavior without the constraint that it has
to be a subclass. See the code below for a better understanding of dynamic
typing in Python:
"""
x = 5  # type of x is an integer
print(type(x))

x = "Educative"  # type of x is now string
print(type(x))
