#This program will find the area and perimeter of Rect.
#This program is done by Gracey Chapadia - 8739519


#define class
class Rectangle:  

    def __init__(self, rectWidth, rectLength):
        self.rectWidth = rectWidth
        self.rectLength = rectLength

    #getting input
    def getInput(self):
        f'{self.rectLength}'
        f'{self.rectWidth}'

    #method to find perimeter
    def getPerimeter(self):
        per = Rectangle(lengthR,widthR)
        per.getInput()
        global perimeterOfRect
        perimeterOfRect = 2*(lengthR+widthR)
        print("As per given Length and Width perimeter of rectangle is: ",str(perimeterOfRect))        
    
    #method to find area 
    def getArea(self):
        area = Rectangle(lengthR,widthR)
        area.getInput()
        global areaOfRect
        areaOfRect = (lengthR*widthR)
        print("As per given Length and Width area of rectangle is: ",str(areaOfRect))        

    #method to display the result
    def showResult(self):
        objectC = Rectangle(widthR,lengthR)
        objectC.getArea()
        objectC.getPerimeter()

#getting input from user
print("Find area and perimeter of rectangle here!\n")
widthR = int(input("Enter width of the Rectangle: ")) 
lengthR = int(input("Enter length of the Rectangle: "))  

#created class object
ClassObj = Rectangle(widthR,lengthR)

#called the display function to show the output
ClassObj.showResult()