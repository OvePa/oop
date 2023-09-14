"""
Syntax
To declare a method as a class method, we use the decorator @classmethod.
< cls > is used to refer to the class just like < self > is used to refer to the
object of the class. You can use any other name instead of < cls >, but < cls >
is used as per convention, and we will continue to use this convention.
"""


class Player:
    teamName = "Liverpool"  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())
