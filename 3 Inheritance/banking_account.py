class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate


if __name__ == "__main__":
    a = Account("Mark", 5000)
    print(a.title)
    print(a.balance)
    a = SavingsAccount("Mark", 5000, 5)
    print(a.title)
    print(a.balance)
    print(a.interestRate)
