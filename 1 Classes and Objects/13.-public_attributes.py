"""
Access Modifiers

In Python, we can impose access restrictions on different data members and member
functions. The restrictions are specified through access modifiers. Access
modifiers are tags we can associate with each member to define which parts of
the program can access it directly.

There are two types of access modifiers in Python. Let’s take a look at them
one by one.

-> Public attributes
Public attributes are those that can be accessed inside the class and outside
the class.

Technically in Python, all methods and properties in a class are publicly
available by default. If we want to suggest that a method should not be used
publicly, we have to declare it as private explicitly.

Below is an example to implement public attributes:
"""


class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)
