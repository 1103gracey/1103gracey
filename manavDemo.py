# print("Hello This is my Demo Program.")
# print("I am going to make a separate functions for maths.")
# print("Functions like Add Sub Div Mul")

def add():
    print ("please enter the two digits for addition.")
    n1 = float (input())
    n2 = float (input())
    print ("addition for "+ str(n1) + " and " + str(n2) +" is: " + str (n1 + n2))

def sub():
    print ("please enter the two digits for Substraction.")
    n1 = float (input())
    n2 = float (input())
    print ("Substraction for "+ str(n1) + " and " + str(n2) +" is: " + str (n1 - n2))

def div():
    print ("please enter the two digits for Division.")
    n1 = float (input())
    n2 = float (input())
    print ("Division for "+ str(n1) + " and " + str(n2) +" is: " + str (n1 / n2))

def mul():
    print ("please enter the two digits for Multiplication.")
    n1 = float (input())
    n2 = float (input())
    print ("Multiplication for "+ str(n1) + " and " + str(n2) +" is: " + str (n1 * n2))


print ("welcome to walmart")
print("_______________________________")

print("count your two items price")
add()
print("_______________________________")

print("Compare price for two items")
sub()

print("_______________________________")
print("Multiply your itmes price")
mul()

print("_______________________________")
print("Divide your items price")
div()
