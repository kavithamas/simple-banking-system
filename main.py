class BankAccount():
    defaultAccountNumber = 1  # class attribute

    def __init__(self, name, Balance=0):
        self.name = name
        self.Balance = Balance
        self.bank = 'SBI'
        self.branchName = 'Adambakkam'
        self.accountNumber = BankAccount.defaultAccountNumber
        BankAccount.defaultAccountNumber += 1

    def deposit(self, amount):
        self.Balance += amount

    def withdraw(self, amount):
        if self.Balance < amount:  # Check if balance is sufficient
            print("Not Enough Money")
        else:
            self.Balance -= amount
            return f'Dear {self.name}! your withdrawal amount is {amount}\nYour remaining balance is {self.Balance}\nThank you for using "{self.bank} {self.branchName}" branch.'

    def getBalance(self):
        return f'Dear {self.name}! your balance amount is {self.Balance} rupees.'

# Example usage
myObj = BankAccount('George', 1000)
myObj.deposit(1000)
print(myObj.getBalance())

