class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        result = self.phy + self.chem + self.bio
        return result

    def percentage(self):
        mo = self.totalObtained()
        result = (mo / 300) * 100
        return result


if __name__ == "__main__":
    Mark = Student("Mark", 80, 90, 40)
    print(Mark.totalObtained())
    print(Mark.percentage())
