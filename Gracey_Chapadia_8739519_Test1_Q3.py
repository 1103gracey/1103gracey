#This program will demonstrate the use of object oriented programming with the use of classes.
#This program is done by Gracey Chapadia - 8739519

class Tempratures:  

    def __init__(self, cityName, Temprature1, Temprature2, Temprature3):
        self.cityName = cityName
        self.Temprature1 = Temprature1
        self.Temprature2 = Temprature2
        self.Temprature3 = Temprature3

    def enterTemp(self):
        f'{self.cityName}'
        f'{self.Temprature1}'
        f'{self.Temprature2}'
        f'{self.Temprature3}'

    def DisplayTemp(self):
        dis1 = Tempratures(city1, temp1City1, temp2City1, temp3City1)
        dis1.enterTemp()
        print(dis1.cityName, dis1.Temprature1, dis1.Temprature2, dis1.Temprature3)
        
        dis2 = Tempratures(city2, temp1City2, temp2City2, temp3City2)
        dis2.enterTemp()
        print(dis2.cityName, dis2.Temprature1, dis2.Temprature2, dis2.Temprature3)
        
        dis3 = Tempratures(city3, temp1City3, temp2City3, temp3City3)
        dis3.enterTemp()
        print(dis3.cityName, dis3.Temprature1, dis3.Temprature2, dis3.Temprature3)
    
    def calcAverageTemp(self):
        avg1 = Tempratures(city1,temp1City1,temp2City1,temp3City1)
        print(str(f'{self.Temprature1}')+str(f'{self.Temprature1}')+str(f'{self.Temprature1}')/3)

city1 = str(input("First City Name: "))
temp1City1 = float(input("Enter Temp of Monday: ")) 
temp2City1 = float(input("Enter Temp Wednesday: ")) 
temp3City1 = float(input("Enter Temp Friday: ")) 

ClassObj = Tempratures(city1,temp1City1,temp2City1,temp3City1)

city2 = str(input("Second City Name: "))
temp1City2 = float(input("Enter Temp of Monday: ")) 
temp2City2 = float(input("Enter Temp of Wednesday: ")) 
temp3City2 = float(input("Enter Temp of Friday: ")) 

ClassObj2 = Tempratures(city1,temp1City2,temp2City2,temp3City2)

city3 = str(input("Third City Name: "))
temp1City3 = float(input("Enter Temp of Monday: ")) 
temp2City3 = float(input("Enter Temp of Wednesday: ")) 
temp3City3 = float(input("Enter Temp of Friday: ")) 

ClassObj3 = Tempratures(city1,temp1City3,temp2City3,temp3City3)

ClassObj.enterTemp()
ClassObj.DisplayTemp()
ClassObj.calcAverageTemp()
