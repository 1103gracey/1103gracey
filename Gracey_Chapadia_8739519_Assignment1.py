from collections import defaultdict
from typing import DefaultDict

# This program is introduced to calculate the total shirt cost.
# Varieties are provided in shirts with differnt colours.
# In Abby's Merchandizing every t-shirt costing is $9.99, which also includes HST in addition to the total cost of t-shirts.

print("Welcome to Abby's Merchandizing.")

# Asking user for the input string and getting input from user.
print ("Which colour of t-shirt you want?\n") 

# User have been provided options for t-shirt colours.
print ("1. Black\n2. Blue\n3. Red\n4. Grey")

# Input of colour is read by the program as per selection.
choiceColor = int(input())

# User have been provided options for t-shirt .
print ("\nYou require polo t-shirt or a t-shirt?")
print ("Enter '1'for polo t-shirt and '2' for t-shirt.")

# Input of t-shirt is read as per selection.
choiceType = int(input())

# Here, user needs to enter the total number of t-shirts.
print ("\nHow many Tshirt do you want?")
choiceQuantity = int(input())


# Here, each string is defined among the categories of t-shirts, with there return message, they are defined when the input from user calls it.
def Black():
    return "you have selected black colour for your t-shirt."
def Blue():
    return "you have selected blue colour for your t-shirt"
def Red():
    return "you have selected red colour for your t-shirt"
def Grey():
    return "you have selected grey colour for your t-shirt"
def Polo():
    return "you have selected Polo t-shirt"
def Tshirt():
    return "you have selected t-shirt"

# A switcher is supplied for the system that stores and executes t-shirt colours when the user makes a call, controlling the flow of strings.
switcher_one = {
1: Black,
2: Blue,
3: Red,
4: Grey
}

# For the system, a switcher is provided that stores and executes the t-shirt type when the user makes a call.
switcher_two = {
1: Polo,
2: Tshirt,
}

def switchColor(choiceColor):
# Input of t-shirt colour is printed as per selection.
    return switcher_one.get(choiceColor, DefaultDict)()
print(switchColor(choiceColor))

def switchType(choiceType):
    return switcher_two.get(choiceType, DefaultDict)()
# Input of t-shirt type is printed as per selection.
print(switchType(choiceType))

print("You have choosen "+str(choiceQuantity)+" Tshirt")

# As cost of every t-shirt is $9.99, total number of t-shirts are multiplied with 9.99 to get the amount.

beforeHSTTotal = choiceQuantity*9.99
print("Your total cost of tshirts before HST is: $" + str(beforeHSTTotal))

# The total cost of t-shirt also including HST with the amount, so that product of that amount is done with 18 to finalize the total cost of tshirts. 
print("Your total cost of t-shirt with HST is $" + str(beforeHSTTotal*0.13+beforeHSTTotal))