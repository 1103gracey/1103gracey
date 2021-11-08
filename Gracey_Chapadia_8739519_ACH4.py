from typing import DefaultDict
from collections import defaultdict

#This program will demonstrate the use of object oriented programming with the use of classes.
#This program is done by Gracey Chapadia - 8739519

class Calculator:  

    def __init__(self, inputDigitOne, inputDigitTwo):
        self.inputDigitOne = inputDigitOne
        self.inputDigitTwo = inputDigitTwo

    def gettingInput(self):
        f'{self.inputDigitOne}'
        f'{self.inputDigitTwo}'

    def addition(self):
        add = Calculator(InputOne, InputTwo)
        add.gettingInput()
        addAns = add.inputDigitOne+add.inputDigitTwo
        print (str(addAns))

    def substraction(self):
         sub = Calculator(InputOne, InputTwo)
         sub.gettingInput()
         subAns = sub.inputDigitOne-sub.inputDigitTwo
         print (str(subAns))

    def multiplication(self):
        mul = Calculator(InputOne, InputTwo)
        mul.gettingInput()
        mulAns = mul.inputDigitOne*mul.inputDigitTwo
        print (str(mulAns))

    def division(self):
        div = Calculator(InputOne, InputTwo)
        div.gettingInput()
        divAns = div.inputDigitOne/div.inputDigitTwo
        print (str(divAns))

    def modulusDivision(self):
        mdiv = Calculator(InputOne, InputTwo)
        mdiv.gettingInput()
        mdivAns = mdiv.inputDigitOne%mdiv.inputDigitTwo
        print (str(mdivAns))

print("What kind of mathematical operation do you want to perform?")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulus Division")

print("Enter Your Choice: ")
choiceType = int(input())

InputOne = int(input("First Digit: "))
InputTwo = int(input("Second Digit: ")) 

ClassObj = Calculator(InputOne, InputTwo)

switcher = {
1: ClassObj.addition,
2: ClassObj.substraction,
3: ClassObj.multiplication,
4: ClassObj.division,
5: ClassObj.modulusDivision
}

def switchCalc(choiceType):
    return switcher.get(choiceType, None)()
print(switchCalc(choiceType))