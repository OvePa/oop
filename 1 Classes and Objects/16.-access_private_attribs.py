"""
Accessing private attributes in the main code
As discussed above, it is not common to have private variables in Python.

Properties and methods with the __ prefix are usually present to make sure that
the user does not carelessly access them. Python allows for free hand to the
user to avoid any future complications in the code. If the user believes it is
absolutely necessary to access a private property or a method, they can access
it using the _<ClassName> prefix for the property or method. An example of this
is shown below:
"""


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property

Job = Employee(123, 34564)
print(Job._Employee__salary)
