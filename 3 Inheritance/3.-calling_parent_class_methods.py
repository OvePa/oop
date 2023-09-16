"""
Calling the parent class methods
Just like properties, super() is also used with methods. Whenever a parent class
and the immediate child class have any methods with the same name, we use
super() to access the methods from the parent class inside the child class.
"""


class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
