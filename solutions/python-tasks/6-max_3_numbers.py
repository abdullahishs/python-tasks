#!/usr/bin/env python3

def max_number():
    numbers = "Enter 3 numbers separated by a comma"
    numbers += "(type 'q' to quit at any time): "
    active = True
    nums = []
    while active == True:
        x = input (numbers)
        if x == 'q':
            active = False
        else:
            num = x.split(",")
            for x in num:
                y = (int(x))
                nums.append(y)
            print (max(nums))
            
max_number()
    
