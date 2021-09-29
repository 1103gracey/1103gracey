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

# Here, each string is defined among the categories of t-shirts, with there return message, they are defined when the input from user calls it.
def Black():
    return "you have selected black colour for your t-shirt."
def Blue():
    return "you have selected blue colour for your t-shirt"
def Red():
    return "you have selected red colour for your t-shirt"
def Grey():
    return "you have selected grey colour for your t-shirt"

# A switcher is supplied for the system that stores and executes t-shirt colours when the user makes a call, controlling the flow of strings.
switcher = {
1: Black,
2: Blue,
3: Red,
4: Grey
}

def switchColor(choiceColor):
    return switcher.get(choiceColor, DefaultDict)()

# Input of t-shirt colour is printed as per selection.
print(switchColor(choiceColor))

