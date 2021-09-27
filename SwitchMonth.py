from collections import defaultdict
from typing import DefaultDict


print ("select your bday month")

print ("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n")
print ("---------------------------------------")

choice = int(input())

def jan():
    return "your bday month is jan"

def feb():
    return "your bday month is feb"

def mar():
    return "your bday month is mar"

def apr():
    return "your bday month is apr"

def may():
    return "your bday month is may"

def jun():
    return "your bday month is jun"

def jul():
    return "your bday month is jul"

def aug():
    return "your bday month is aug"

def sep():
    return "your bday month is sep"

def oct():
    return "your bday month is oct"

def nov():
    return "your bday month is nov"

def dec():
    return "your bday month is dec"

switcher = {
1: jan,
2: feb,
3: mar,
4: apr,
5: may,
6: jun,
7: jul,
8: aug,
9: sep,
10: oct,
11: nov,
12:dec
}

def switch(choice):
    return switcher.get(choice, DefaultDict)()
print(switch(choice))
