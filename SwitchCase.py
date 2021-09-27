from typing import DefaultDict


print("Welcome to walmart kiosk")
print("_______________________________________________________________")

print("Enter your choice from one to four:")
print("1.add\n2.sub\n3.mul\n4.div")
print("_______________________________________________________________")

choice = int(input())


def add():
    print("Enter your item Prices:")
    print("_______________________________________________________________")

    n1 = float(input())
    n2 = float(input())
    
    ans = n1+n2
    print ("addition for "+ str(n1) + " and " + str(n2) +" is: ")
    print("_______________________________________________________________")
    return ans

def sub():
    print("Enter your item Prices:")
    print("_______________________________________________________________")

    n1 = float(input())
    n2 = float(input())
    
    ans = n1-n2
    print ("substraction for "+ str(n1) + " and " + str(n2) +" is: ")
    print("_______________________________________________________________")
    return ans

def div():
    print("Enter your item Prices:")
    print("_______________________________________________________________")

    n1 = float(input())
    n2 = float(input())

    ans = n1/n2

    print ("division for "+ str(n1) + " and " + str(n2) +" is: ")
    print("_______________________________________________________________")
    return ans

def mul():
    print("Enter your item Prices:")
    print("_______________________________________________________________")

    n1 = float(input())
    n2 = float(input())
    
    ans = n1*n2
    print ("multiplication for "+ str(n1) + " and " + str(n2) +" is: ")
    print("_______________________________________________________________")
    return ans

switcher = {
    1: add,
    2: sub,
    3: mul,
    4: div
}

def switch(choice):
    return switcher.get(choice, DefaultDict)()
print(switch(choice))



