from typing import DefaultDict
from collections import defaultdict

#This program will demonstrate the use of object oriented programming with the use of classes.
#This program is done by Gracey Chapadia - 8739519


#defining CLass
class Largestvalue:  

    #defining init method
    def __init__(self, inputDigitOne, inputDigitTwo, inputDigitThree):
        self.inputDigitOne = inputDigitOne
        self.inputDigitTwo = inputDigitTwo
        self.inputDigitThree = inputDigitThree

    #defining input method
    def gettingInput(self):
        f'{self.inputDigitOne}'
        f'{self.inputDigitTwo}'
        f'{self.inputDigitThree}'

    #defining maxvalue method
    def maxValue(self):
        max = Largestvalue(InputOne, InputTwo, InputThree)
        max.gettingInput()
        
        if(max.inputDigitOne > max.inputDigitTwo and max.inputDigitOne>max.inputDigitThree):
            print("Large number is:" + str(max.inputDigitOne))
        elif(max.inputDigitTwo > max.inputDigitOne and max.inputDigitTwo>max.inputDigitThree):
            print("Large number is:" + str(max.inputDigitTwo))
        else:
            print("Large number is:" + str(max.inputDigitThree))

#giving prompt to the user to choose the operation
print("Enter three numbers: ")

#getting input from user
InputOne = float(input("First: ")) 
InputTwo = float(input("Second: ")) 
InputThree = float(input("Third: ")) 

#class object created
ClassObj = Largestvalue(InputOne, InputTwo, InputThree)

#Class method calling
ClassObj.maxValue()