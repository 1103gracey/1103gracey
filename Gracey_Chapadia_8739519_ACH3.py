# This program is about the sum of square of only even numbers less than the the input provided by the user.
# This program is coded by Gracey Chapadia.

# dividing the counts in number so that the differntiation in even and odd numbers is done at first.
evenCount, oddCount = 0, 0
even = []
odd = []
# Providing the first digit for the count. 
startingDigit = 1
# Last digit will be the user input so that that value is asked to the user till which the calculation is done.
endingDigit = int(input("Enter the ending value: "))

# Loop is created for even count and then the if statement is provided, if it satisfies even digit are counted.
# Range is created so that exact number of digits are calculated.
for i in range(startingDigit,endingDigit+1):
    if i % 2 == 0:
        evenCount += 1
        even.append(i)

# Total sum is kept 0 at first after calculation the main value id printed.
sum = 0
# Here, in for loop the formula to count sum of sqaure of even number is counted.
for i in range (evenCount
 + 1):
    sum += (2 * i) * (2 * i)

print ("Your answer is: "+ str(sum))
