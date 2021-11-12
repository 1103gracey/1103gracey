from typing import DefaultDict
from collections import defaultdict

#This program will demonstrate the use of object oriented programming with the use of classes.
#This program is done by Gracey Chapadia - 8739519

#defining factorial function for the program
def factorial(n):
    digit=1

    for i in range(1, n+1):
        digit=digit*i
    return digit

inputUser=int(input("Enter integer digit to find factorial of it: "))

outputAns=factorial(inputUser)

print("Your answer is: " + str(outputAns))