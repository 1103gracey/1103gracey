#This program will demonstrate the calculating total number of counts in givrn string.
#This program is done by Gracey Chapadia - 8739519


inputString = 'Lorem ipsum doflor szit ametß, consqecytetu$r adipibsching elit, sed do eiusmod tewmporα incid6kgidunt ut labq8ore et café gracey chapadia 8739519 dolore_ magna aliqua. Purus! sit{|}~ \t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. Penaxtibus et'

numberValue = sum(count.isdigit() for count in inputString)

alphanumbericValue = sum(count.isalnum() for count in inputString)

spaceValue = sum(count.isspace() for count in inputString)

nonAlphanumbericValue = len(inputString) - numberValue -alphanumbericValue - spaceValue


print("Found " + str(inputString.count('g'))+ " matches of letter G.")
print("Found " + str(numberValue) + " matches of digits.")
print("Found " + str(alphanumbericValue) + " matches of AlphaNumeric characters.")
print("Found " + str(nonAlphanumbericValue) + " matches of Non AlphaNumeric characters.")
print("Found " + str(spaceValue) + " number of spaces.")