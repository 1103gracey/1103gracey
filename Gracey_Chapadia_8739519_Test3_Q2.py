#This program will find the area and perimeter of Rect.
#This program is done by Gracey Chapadia - 8739519

class Rectangle:  

    def __init__(self, rectWidth, rectLength):
        self.rectWidth = rectWidth
        self.rectLength = rectLength

    def getInput(self):
        f'{self.rectLength}'
        f'{self.rectWidth}'

    def getPerimeter(self):
        per = Rectangle(lengthR,widthR)
        per.getInput()
        global perimeterOfRect
        perimeterOfRect = 2*(lengthR+widthR)
        print("As per given Length and Width perimeter of rectangle is: ",str(perimeterOfRect))        
    
    def getArea(self):
        area = Rectangle(lengthR,widthR)
        area.getInput()
        global areaOfRect
        areaOfRect = (lengthR*widthR)
        print("As per given Length and Width area of rectangle is: ",str(areaOfRect))        

    def showResult(self):
        objectC = Rectangle(widthR,lengthR)
        objectC.getArea()
        objectC.getPerimeter()


print("Find area and perimeter of rectangle here!\n")
widthR = int(input("Enter width of the Rectangle: ")) 
lengthR = int(input("Enter length of the Rectangle: "))  

ClassObj = Rectangle(widthR,lengthR)
ClassObj.showResult()