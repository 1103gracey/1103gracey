import random
#This program will find the area and perimeter of Rect.
#This program is done by Gracey Chapadia - 8739519

listofQuestionAnswer = [
    ["What is the biggest animal in the world?:\n", "Blue Whale"],
    ["What is the capital of Canada?:\n", "Ottawa"],
    ["how many provinces and territories in canada? (In Digits):\n", "10"],
    ["What does IP stand for?:\n", "Internet Protocol"],
    ["What's a baby rabbit called?:\n", "Kit"],
    ["Who painted the Mona Lisa?:\n", "Leonardo da Vinci"],
    ["How many bones does a shark have?:\n", "None"],
    ["What grain is the Japanese spirit Sake made from?:\n", "Rice"],
    ["Who invented the World Wide Web in 1990?:\n", "Tim Berners-Lee"],
    ["What is the multiplication of 2*5?:\n",  "10"],
]

class myQuizeGame:

    def __init__(self, studentName, playerData):
        self.studentName = studentName
        self.playerData = playerData

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

