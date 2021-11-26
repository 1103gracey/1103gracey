from typing import DefaultDict
from collections import defaultdict

# This program will demonstrate the use of object oriented programming with the use of classes.
# This program is done by Gracey Chapadia - 8739519
# Abby’s Merchandizing (AM) is a very busy place and needs some software to help with orders of clothing
# This program is introduced to calculate the total shirt cost using object oriented programming.


class ClothingType:
    # Here, each string is defined among the categories of t-shirts, with there return message, they are defined when the input from user calls it.
    def Trouser(self):
        return "you have selected trouser."

    def Tshirt(self):
        return "you have selected t-shirt."

print("Welcome to Abby's Merchandizing.")

print("Which age group you are belong to: Student or Senior?")
print("Your answer must be in S/s = Senior or Y/y = Student.")

ageGroupInput = str(input())

# Asking user for the input string and getting input from user.
print("What would you like to purchase?\n")

# User have been provided options for t-shirt colours.
print("1. Tshirt\n2. Trouser")

print("\nEnter your choice here: ")

# Input of colour is read by the program as per selection.
choiceClothType = int(input())

# Function created to define the object of class.
objClothType = ClothingType()

switcher_one_cloth_type = {
    1: objClothType.Tshirt,
    2: objClothType.Trouser
}


def switchClothType(choiceClothTypesw):
    # Input of t-shirt colour is printed as per selection.
    return switcher_one_cloth_type.get(choiceClothTypesw, DefaultDict)()    
print(switchClothType(choiceClothType))
    
def inputTshirt():

    global choiceQuantityTshirt
    global totalBeforeDiscTshirt

    totalBeforeDiscTshirt = 0

    # Asking user for the input string and getting input from user.
    print ("Which colour of t-shirt you want?\n") 

    # User have been provided options for t-shirt colours.
    print ("1. Black\n2. Blue\n3. Red\n4. Grey")

    # Input of colour is read by the program as per selection.
    choiceColor = int(input())

    # User have been provided options for t-shirt .
    print ("\nYou require polo t-shirt or a t-shirt?")
    print ("\n1. polo - $9.99\n2. t-shirt - $9.99")
    print ("Enter '1'for polo t-shirt and '2' for t-shirt.")

    # Input of t-shirt is read as per selection.
    choiceType = int(input())

    # Here, user needs to enter the total number of t-shirts.
    print ("\nHow many Tshirt do you want?")
    print ("\nCurrent offers \n 1. Student will get 10% discount\n If you purchase 3 or more items student and senior will get quantity discount of 15%")

    # Function created to define the object of class.
    choiceQuantityTshirt = int(input())


    # Here, each string is defined among the categories of t-shirts, with there return message, they are defined when the input from user calls it.
    def Black():
        return "you have selected black colour for your t-shirt."
    def Blue():
        return "you have selected blue colour for your t-shirt."
    def Red():
        return "you have selected red colour for your t-shirt."
    def Grey():
        return "you have selected grey colour for your t-shirt."
    def Polo():
        return "you have selected Polo t-shirt."
    def Tshirt():
        return "you have selected t-shirt."

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

    print("You have choosen "+str(choiceQuantityTshirt)+" Tshirt")

    print("Would you link to purchase trouser? Answer: Y/N || y/n")
    userAnswer = str(input())
    if(userAnswer == "Y" or userAnswer == "y"):
        inputTrouser()
    else:
        print("Thank you for your interest!")

#Class Trouser has been created in which its colour and type are given.
def inputTrouser():

    global choiceQuantityTrouser
    global totalBeforeDiscTrouser

    totalBeforeDiscTrouser = 0

    # Asking user for the input string and getting input from user.
    print ("Which colour of trouser you want?\n") 

    # User have been provided options for t-shirt colours.
    print ("1. Black\n2. Blue\n3. Grey")
    
    # Input of colour is read by the program as per selection.
    choiceColor = int(input())
    
    # User have been provided options for t-shirt .
    print ("\nYou require Denim Trouser or a Cotton one?")
    print ("\n1. Denim - $11.99\n2. Cotton - $11.99")
    print ("Enter '1'for Denim and '2' for Cotton.")
    
    # Input of t-shirt is read as per selection.
    choiceType = int(input())
    
    # Here, user needs to enter the total number of t-shirts.
    print ("\nHow many Trousers do you want?")
    print ("\nCurrent offers \n 1. Student will get 10% discount\n If you purchase 3 or more items student and senior will get quantity discount of 15%")

    choiceQuantityTrouser = int(input())
    
    # Here, each string is defined among the categories of t-shirts, with there return message, they are defined when the input from user calls it.
    def Black():
        return "you have selected black colour for your trouser."
    def Blue():
        return "you have selected blue colour for your trouser."
    def Grey():
        return "you have selected grey colour for your trouser."
    def Denim():
        return "you have selected denim trouser."
    def Cotton():
        return "you have selected cotton trouser."
    
    # A switcher is supplied for the system that stores and executes t-shirt colours when the user makes a call, controlling the flow of strings.
    switcher_one = {
    1: Black,
    2: Blue,
    3: Grey
    }
    
    # For the system, a switcher is provided that stores and executes the t-shirt type when the user makes a call.
    switcher_two = {
    1: Denim,
    2: Cotton,
    }
    
    def switchColor(choiceColor):
    # Input of t-shirt colour is printed as per selection.
        return switcher_one.get(choiceColor, DefaultDict)()
    print(switchColor(choiceColor))
    
    def switchType(choiceType):
        return switcher_two.get(choiceType, DefaultDict)()
    # Input of t-shirt type is printed as per selection.
    print(switchType(choiceType))
    
    print("You have choosen "+str(choiceQuantityTrouser)+" Trousers")

    print("Would you link to purchase tshirt? Answer: Y/N || y/n")
    userAnswer = str(input())
    if(userAnswer == "Y" or userAnswer == "y"):
        inputTshirt()
    else:
        print("Thank you for your interest!")

#condition to check input category
if(choiceClothType == 1):
    inputTshirt()
    totalBeforeDiscTshirt = choiceQuantityTshirt*9.99
    print("Your total cost of tshirts before discount is: $" + str(totalBeforeDiscTshirt))
    
    #condition to check age category
    if(ageGroupInput == "y" or ageGroupInput == "Y"):
        print("Congratulations you are eligible to get student discount of 10%!")
         
         #condition to check what discount user will get
        if(choiceQuantityTshirt>=3 and choiceQuantityTrouser < 3):
            print("You are eligible for both discount!")
            studentDisc = totalBeforeDiscTshirt*0.1
            quantityDisc = totalBeforeDiscTshirt*0.15
            discDigit = studentDisc+quantityDisc
            discAmtTs = totalBeforeDiscTshirt - discDigit
            HSTtax = discAmtTs*0.13
            finalHSTTax = HSTtax+discAmtTs
            print("\n__________________________________________________\nBILL SUMMARY\n__________________________________________________")
            print("You purchased "+ str(choiceQuantityTshirt) +" tshirt.")
            print("You purchased "+ str(choiceQuantityTrouser) +" trouser.")
            print("Total price is: $" + (str(totalBeforeDiscTshirt)+(str(totalBeforeDiscTrouser))))
            print("Total diduction: $" + str(discDigit))
            print("Your final price after applying both discounts is: $" + str(discAmtTs))
            print("Your final price after adding tax is: $" + str(finalHSTTax))

        #condition to check what discount user will get
        elif(choiceQuantityTshirt<3 and choiceQuantityTrouser >= 3):
            print("You are eligible for both discount!")
            studentDisc = totalBeforeDiscTrouser*0.1
            quantityDisc = totalBeforeDiscTrouser*0.15
            discDigit = studentDisc+quantityDisc
            discAmtTr = totalBeforeDiscTrouser - discDigit
            HSTtax = discAmtTr*0.13
            finalHSTTax = HSTtax+discAmtTr
            print("\n__________________________________________________\nBILL SUMMARY\n__________________________________________________")
            print("You purchased "+ str(choiceQuantityTshirt) +" tshirt.")
            print("You purchased "+ str(choiceQuantityTrouser) +" trouser.")
            print("Total price is: $" + (str(totalBeforeDiscTshirt)+(str(totalBeforeDiscTrouser))))
            print("Total diduction: $" + str(discDigit))
            print("Your final price after applying both discounts is: $" + str(discAmtTr))
            print("Your final price after adding tax is: $" + str(finalHSTTax))

        #condition to check what discount user will get
        elif(choiceQuantityTshirt >= 3 and choiceQuantityTrouser >= 3):
            print("You are eligible for both discount!")
            discAmtAll = totalBeforeDiscTrouser + totalBeforeDiscTshirt
            discAmtPrice = discAmtAll * 0.25
            HSTtax = discAmtPrice*0.13
            finalHSTTax = HSTtax+discAmtPrice
            print("\n__________________________________________________\nBILL SUMMARY\n__________________________________________________")
            print("You purchased "+ str(choiceQuantityTshirt) +" tshirt.")
            print("You purchased "+ str(choiceQuantityTrouser) +" trouser.")
            print("Total price is: $" + (str(totalBeforeDiscTshirt)+(str(totalBeforeDiscTrouser))))
            print("Your final price after applying both discounts is: $" + str(discAmtPrice))
            print("Your final price after adding tax is: $" + str(finalHSTTax))
    else:

        #condition to check what discount user will get
        if(choiceQuantityTshirt>=3 and choiceQuantityTrouser < 3):
            print("You are eligible for quanity discount!")
            quantityDisc = totalBeforeDiscTshirt*0.15
            discDigit = quantityDisc
            discAmtTs = totalBeforeDiscTshirt - discDigit
            HSTtax = discAmtTs*0.13
            finalHSTTax = HSTtax+discAmtTs
            print("\n__________________________________________________\nBILL SUMMARY\n__________________________________________________")
            print("You purchased "+ str(choiceQuantityTshirt) +" tshirt.")
            print("You purchased "+ str(choiceQuantityTrouser) +" trouser.")       
            print("Total price is: $" + (str(totalBeforeDiscTshirt)+(str(totalBeforeDiscTrouser))))
            print("Total diduction: $" + str(discDigit))
            print("Your final price after applying discount is: $" + str(discAmtTs))
            print("Your final price after adding tax is: $" + str(finalHSTTax))

        #condition to check what discount user will get
        elif(choiceQuantityTshirt<3 and choiceQuantityTrouser >= 3):
            print("You are eligible for quantity discount!")
            quantityDisc = totalBeforeDiscTrouser*0.15
            discDigit = quantityDisc
            discAmtTr = totalBeforeDiscTrouser - discDigit
            HSTtax = discAmtTr*0.13
            finalHSTTax = HSTtax+discAmtTr
            print("\n__________________________________________________\nBILL SUMMARY\n__________________________________________________")
            print("You purchased "+ str(choiceQuantityTshirt) +" tshirt.")
            print("You purchased "+ str(choiceQuantityTrouser) +" trouser.")
            print("Total price is: $" + (str(totalBeforeDiscTshirt)+(str(totalBeforeDiscTrouser))))
            print("Total diduction: $" + str(discDigit))
            print("Your final price after applying both discounts is: $" + str(discAmtTr))
            print("Your final price after adding tax is: $" + str(finalHSTTax))

        #condition to check what discount user will get
        elif(choiceQuantityTshirt >= 3 and choiceQuantityTrouser >= 3):
            print("You are eligible for quantity discount!")
            discAmtAll = totalBeforeDiscTrouser + totalBeforeDiscTshirt
            discAmtPrice = discAmtAll * 0.15
            HSTtax = discAmtPrice*0.13
            finalHSTTax = HSTtax+discAmtPrice
            print("\n__________________________________________________\nBILL SUMMARY\n__________________________________________________")
            print("Total price is: $" + (str(totalBeforeDiscTshirt)+(str(totalBeforeDiscTrouser))))
            print("Your final price after applying both discounts is: $" + str(discAmtPrice))
            print("Your final price after adding tax is: $" + str(finalHSTTax))
    
elif(choiceClothType == 2):
    inputTrouser()
    print(choiceQuantityTrouser)
    totalBeforeDiscTrouser = choiceQuantityTrouser*11.99
    print("Your total cost of trousers before discount is: $" + str(totalBeforeDiscTrouser))
else:
    print ("Wrong Input!")