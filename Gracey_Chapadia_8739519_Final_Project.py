import random
#This program will find the area and perimeter of Rect.
#This program is done by Gracey Chapadia - 8739519

listofQuestionAnswer = [
    ["What star is in the center of the solar system?:\n", "Sun"],
    ["What is the 3rd planet of the solar system?:\n", "Earth"],
    ["What can be broken, but is never held?:\n", "Promise"],
    ["What part of the body you use to smell?:\n", "Nose"],
    ["How many days in one year?:\n", "365"],
    ["How many letters in the alphabet?:\n", "26"],
    ["Rival of Intel?:\n", "AMD"],
    ["No.8 element on periodic element?:\n", "Oxygen"],
    ["What is the galaxy that contains our solar system?:\n", "Milky Way"],
    ["What animal is the king of the jungle?:\n",  "Lion"],
]

class myQuizeGame:

    def __init__(self, studentName, playerData):
        self.studentName = studentName
        self.playerData = playerData

    #getting input
    def getInput(self):
        f'{self.studentName}'
        f'{self.playerData}'

    def mainFunction():
        inu = myQuizeGame(sName,listofQuestionAnswer)
        inu.getInput()

        global playerScore
        playerScore = 0

        for q, a in inu.playerData:
            playerGuess = input(q)
            if playerGuess.lower() == a.lower():
                print("Hurrey!\nYou Guess it.\n\n")
                playerScore += 1
            else:
                print("SOrry!\nYour answer is wrong.\n\n")
        print("\n\nhey, " + str(inu.studentName) + " your score is: " + str(playerScore) + "\n")
        return playerScore

print("Welcome to the Conestoga College General Knowledge Tuesday Trivia!\n\n")
 
sName = input("hey condor!\n\nWrite your name here: ")
print("\n\nYour Quiz has begin...\n\n")

ClassObj = myQuizeGame(sName, listofQuestionAnswer)
random.shuffle(listofQuestionAnswer)
myQuizeGame.mainFunction()

if playerScore == 10:
    print("Congratulations, " + sName + "!!!" + "\nYou won the $100 Amazon gift card.")
else:
    print("Thnank you, " + sName)

