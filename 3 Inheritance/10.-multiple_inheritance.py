"""
Multiple inheritance
When a class is derived from more than one base class, i.e., when a class has
more than one immediate parent class, it is called multiple inheritance.
"""


class CombustionEngine:
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine:
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity


# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()

print(HybridEngine.__mro__)
