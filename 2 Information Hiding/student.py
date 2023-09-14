class Student:
    def __init__(self, name=None, rollNumber=None):
        self.__name = name
        self.__rollNumber = rollNumber

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


if __name__ == "__main__":
    steve = Student()
    steve.setName("Steve")
    steve.setRollNumber(234)
    print("Name:", steve.getName())
    print("RollNumber:", steve.getRollNumber())
