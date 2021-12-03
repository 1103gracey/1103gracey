n = int(input("Enter the ending number: "))
sum = 0
m = 0

#write 1 instead of 2
for num in range(1, n + 1, 1):
    sum = sum + num

print("The sum of the first", n, "numbers is: ", sum)

#remove n+1 and add only n to the code to find the average
average = sum / n

#change n instead of m, there is no need of m in the code
print("The average of the first", n, "numbers is: ", average)