""" Python code"""
""" For loop goes trough all the numbers from 1 to 1000. Using if function if i is divisible by 3 or 5.
If yes then the number 'i' is added to the sum of other numbers that are multiples of 3 and 5. 
After the loop is finished numbers sum is displayed on the screen."""

sum = 0
for i in range (1, 1000):
    if i%3 or i%5:
      sum = sum + i
      
print sum
