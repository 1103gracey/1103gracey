from typing import DefaultDict
from collections import defaultdict

#This program will demonstrate the use of object oriented programming with the use of classes.
#This program is done by Gracey Chapadia - 8739519


#defining CLass

class Calculator:  


    #defining init method
    def __init__(self, inputDigitOne, inputDigitTwo):
        self.inputDigitOne = inputDigitOne
        self.inputDigitTwo = inputDigitTwo

    #defining input method
    def gettingInput(self):
        f'{self.inputDigitOne}'
        f'{self.inputDigitTwo}'

    #defining addition method
    def addition(self):
        add = Calculator(InputOne, InputTwo)
        add.gettingInput()
        addAns = add.inputDigitOne+add.inputDigitTwo
        print (str(addAns))

    #defining substraction method
    def substraction(self):
         sub = Calculator(InputOne, InputTwo)
         sub.gettingInput()
         subAns = sub.inputDigitOne-sub.inputDigitTwo
         print (str(subAns))

    #defining multiplication method
    def multiplication(self):
        mul = Calculator(InputOne, InputTwo)
        mul.gettingInput()
        mulAns = mul.inputDigitOne*mul.inputDigitTwo
        print (str(mulAns))

    #defining division method
    def division(self):
        div = Calculator(InputOne, InputTwo)
        div.gettingInput()
        divAns = div.inputDigitOne/div.inputDigitTwo
        print (str(divAns))

    #defining mpdulus division method
    def modulusDivision(self):
        mdiv = Calculator(InputOne, InputTwo)
        mdiv.gettingInput()
        mdivAns = mdiv.inputDigitOne%mdiv.inputDigitTwo
        print (str(mdivAns))

#giving prompt to the user to choose the operation
print("What kind of mathematical operation do you want to perform?")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulus Division")

#getting choice of the user
print("Enter Your Choice: ")
choiceType = int(input())

#getting input from the user
InputOne = int(input("First Digit: "))
InputTwo = int(input("Second Digit: ")) 

#class object created
ClassObj = Calculator(InputOne, InputTwo)

#switcher created
switcher = {
1: ClassObj.addition,
2: ClassObj.substraction,
3: ClassObj.multiplication,
4: ClassObj.division,
5: ClassObj.modulusDivision
}

#defining the switcher method
def switchCalc(choiceType):
    return switcher.get(choiceType, None)()
print(switchCalc(choiceType))