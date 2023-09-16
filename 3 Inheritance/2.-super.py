"""
What is the super() function?
The use of super() comes into play when we implement inheritance. It is used in
a child class to refer to the parent class without explicitly naming it. It makes
the code more manageable, and there is no need to know the name of the parent
class to access its attributes.
"""
"""
Use cases of the super() function
The super function is used in three relevant contexts:

Accessing parent class properties
Consider the fields named fuelCap defined inside a Vehicle class to keep track 
of the fuel capacity of a vehicle. Another class named Car extends from this 
Vehicle class. We declare a class property inside the Car class with the same 
name, i.e., fuelCap, but with a different value. Now, if we want to refer to 
the fuelCap field of the parent class inside the child class, we will have to 
use the super() function.
"""


class Vehicle:  # Defininf the parent class
    fuelCap = 90


class Car(Vehicle):
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from Vehicle Class:", super().fuelCap)
        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()
obj1.display()
