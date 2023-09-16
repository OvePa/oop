"""
Using with initializers
Another essential use of the function super() is to call the initializer of the
parent class from inside the initializer of the child class.

Note: It is not necessary that the call to super() in a method or an initializer
is made in the first line of the method.
"""


class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass1(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


class ChildClass2(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)  # Does not change the functionality


obj = ChildClass1(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)

obj = ChildClass2(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
