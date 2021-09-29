# This program is about the validation of character strings where it converts lower case into upper one and upper case in to lower one and, this program accepts alpha characters only.
# This program is coded by Gracey Chapadia.

# Asking user for the input string and getrting input from user
print ("please enter the String")
inputOne = str(input())

#cheking condition whether input string is AlphaChar or Not. 
if inputOne.isalpha():

    #If it is aplachar it will check for the lower case
    if inputOne.islower():
        print(inputOne.upper())   
    
    #If it is not lower case it will consider input string as an upper case and convert it into the lower case.
    else: 
        print((inputOne.lower()))
#if condition got false it shows error message.
else:
    print("Wrong Input")