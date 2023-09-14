"""
Private attributes
Private attributes cannot be accessed directly from outside the class but can
be accessed from inside the class.

The aim is to keep it hidden from the users and other classes. Unlike in many
different languages, it is not a widespread practice in Python to keep the data
members private since we do not want to create hindrances for the users. We can
make members private using the double underscore __ prefix

Trying to access private attributes in the main code will generate an error.
An example of this is shown below:

Private properties
Let’s see an example of code for implementing private properties:
"""


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error
