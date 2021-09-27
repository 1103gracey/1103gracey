print ("please enter the String")
inputOne = str(input())

validationVar = inputOne

if validationVar.isalpha():
    if validationVar.islower():
        print(str(validationVar.upper()))   
    else: 
        print((validationVar.lower()))
else:
    print("Wrong Input")