class AnalyseTriangle:
    def _int_(self, sideOne, sideTwo, sideThree):
        self.sideOne = sideOne
        self.sideTwo = sideTwo
        self.sideThree = sideThree

    def validateTriangle(self): 
        input = AnalyseTriangle()

        if input.sideOne == 90 and input.sideTwo == 90 and input.sideThree ==90:

            {
                print ("Equilateral triangle")
            }
        return True

print ("Welcome to triangle validation program")

one = int(input("Enter Side 1:"))
two = int(input("Enter Side 2:"))
three = int(input("Enter Side 3:"))

classobj = AnalyseTriangle(one, two, three)
classobj.validateTriangle()