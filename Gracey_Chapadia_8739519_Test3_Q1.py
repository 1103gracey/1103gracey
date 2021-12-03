from datetime import datetime

#This program will demonstrate the date and time.
#This program is done by Gracey Chapadia - 8739519

currentDateTime = datetime.now()

dateAndTime = currentDateTime.strftime("%m/%d/%Y %H:%M:%S")

print("The current date and time is: ", str(dateAndTime))
