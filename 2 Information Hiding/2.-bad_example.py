class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if (self.userName.lower() == userName.lower()) and (self.password == password):
            print("Access Granted!")
        else:
            print("Invalid Credencials!")


Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"
Steve.login("steve", "6789")

"""
In the above coding example, we can observe that anyone can access, change, or 
print the password and userName fields directly from the main code. This is 
dangerous in the case of this User class because there is no encapsulation of 
the credentials of a user, which means anyone can access their account by 
manipulating the stored data. So, the above code does not follow good coding 
practices.
"""
