#Euler task 19.
#I have to find how many Sundays fell on the first of the month during the twentieth century.

#Number of days in each month through the year
months=[31,28,31,30,31,30,31,31,30,31,30,31]
#initialising variables
d=0
sundays=0
#for loop that goes trough 100 years
for y in range(0,101):
    #It checks if it is divisible by 4 and divisable by 100
    #or if it is divisable by 400
    if (not (1900+y)%4 and (1900+y)%100) or not (1900+y)%400:
      #If one of the above is not, that means it is a leap year and it has 29 days in February
      months[1]=29
    else:
      #Else it is not a leap year and February has 28 days
      months[1]=28
    #for loop that goes trough each month in the year
    for m in months:
        #checks if the first day of a month is sunday
        if (not (d-1)%7 and y>=1):
            sundays+=1

        d+=m

#prints out the answer
print "Number of sundays: ",sundays

