from typing import DefaultDict
from collections import defaultdict

#This program will demonstrate the use of object oriented programming with the use of classes.
#This program is done by Gracey Chapadia - 8739519

#defining CLass
class Account:  

    #defining init method
    def __init__(self, getBalance, currentBalance = 3000):
        self.getBalance = getBalance
        self.currentBalance = currentBalance

    #defining input method
    def gettingInput(self):
        f'{self.getBalance}'

    #defining maxvalue method
    def deposit(self):
        dep = Account(inputAmount)
        dep.gettingInput()
        # global CurrentBalance
        # CurrentBalance = 3000
        print("Your money is deposit successfully!")
        self.currentBalance = self.currentBalance+dep.getBalance
        
            
    def withdrawal(self):
        wtd = Account(amount)
        wtd.gettingInput()
        print("Your money is withdrawn successfully!")
        self.currentBalance = self.currentBalance-wtd.getBalance

    def balance(self):
        self.currentBalance
        print("Your balance is:" + str(self.currentBalance))
        
#getting input from user
inputAmount = float(input("Enter Amount to deposit: ")) 

#class object created
ClassObj = Account(inputAmount)

#Class method calling
ClassObj.deposit()
ClassObj.balance()

print("What do you want to perform? \n\n1.Deposit Money\n2.Withdraw Money")
choiceType = int(input("Choose option from 1 or 2: "))
amount = float(input("Enter Amount: "))

#switcher created
switcher = {
1: ClassObj.deposit,
2: ClassObj.withdrawal,
}

#defining the switcher method
def switchAcc(choiceType):
    return switcher.get(choiceType, None)()
print(switchAcc(choiceType))

ClassObj.balance()