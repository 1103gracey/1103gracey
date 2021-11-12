from typing import DefaultDict
from collections import defaultdict

#This program will demonstrate the use of object oriented programming with the use of function.
#This program is done by Gracey Chapadia - 8739519

#defining factorial function for the program
def factorial(n):
    digit=1

    #applying logic using for loop
    for i in range(1, n+1):
        digit=digit*i
    return digit
#showing prompt messsage to user
inputUser=int(input("Enter integer digit to find factorial of it: "))

#giving value of input to the function parameter and storing result to the outputAns variable 
outputAns=factorial(inputUser)

#showing output message to user
print("Your answer is: " + str(outputAns))