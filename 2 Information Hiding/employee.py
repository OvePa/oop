class Employee:
    def __init__(self, name="", ID=0, department=""):
        # Declare the attributes here
        self.__name = name
        self.__ID = ID
        self.__department = department

    def get_name(self):
        return self.__name

    def set_name(self, x):
        self.__name = x

    def get_ID(self):
        return self.__ID

    def set_ID(self, x):
        self.__ID = x

    def get_department(self):
        return self.__name

    def set_departmen(self, x):
        self.__department = x

    # Create your getter and setter methods here


if __name__ == "__main__":
    s = Employee()
    s.set_name("juan")
    print(s.get_name())
    s.set_ID(23)
    print(s.get_ID())
