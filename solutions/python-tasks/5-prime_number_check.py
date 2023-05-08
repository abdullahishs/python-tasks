#!/usr/bin/env python3

number = "Enter the number you wish to test: "
active = True
while active == True:
    test = input(number)
    if test == 'q':
        active = False        
    for x in range (1,(int(test)/2)+1):
        if int(test) % x == 0:
            print (test + " is a prime number")
            break
        else:
            print (test + " is a prime number")

