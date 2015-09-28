#Euler task 25
#Find the index of the first term in the Fibonacci sequence to contain 1000 digits.
import string

#declare variables
F0 = 0
F1 = 1
num = 0
index = 1

#while loop that check if the number is no longer then 1000 digits
#changes the number into string to get the lenght
while len(str(num))<1000:
    #
    index += 1
    F2 = F0+F1
    F0 = F1
    F1 = F2
    num = F2

print "The index is: ",index