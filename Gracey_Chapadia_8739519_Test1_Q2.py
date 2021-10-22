#This program will count the length of the string.
#This program is done by Gracey Chapadia - 8739519

# Asking user for the input string and getrting input from user
print ("please enter the String")
inputFromUser = str(input())

#Using the len and count inbuilt function of Python.
print("\nAnswer is: ") 
print(len(inputFromUser) + inputFromUser.count(" "))
