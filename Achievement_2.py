print ("please enter the String")
inputOne = str(input())

if inputOne.upper().isalpha():
    print(inputOne.lower())
elif inputOne.lower().isalpha(): 
    print(inputOne.upper())
else:
    print("Wrong Input")

