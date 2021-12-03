from datetime import datetime

#This program will demonstrate the date and time.
#This program is done by Gracey Chapadia - 8739519

#making variable which fetch the current date and time
currentDateTime = datetime.now()

#storing result of currentDateTime variable in to the new string and format the result using strftime
dateAndTime = currentDateTime.strftime("%m/%d/%Y %H:%M:%S")

#giving prompt message to the user
print("The current date and time is: ", str(dateAndTime))
