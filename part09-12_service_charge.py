class BankAccount:
    def __init__(self, name: str, number: int, balance: float):
        self.__name = name
        self.__number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        charge = self.__balance*0.01
        self.__balance -= charge

    def deposit(self, amount: float):
        if amount >= 0:
            self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        if amount >= 0:
            self.__balance -= amount
        self.__service_charge()

if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)    