#!/usr/bin/env python3

def case_count():
    name = input("Enter your string to see how many upper or lower case letters it has: ")
    upper_count = 0
    lower_count = 0
    for x in name:
        if x.isupper() == True:
            upper_count = upper_count + 1
        if x.islower() == True:
            lower_count = lower_count + 1
    counted = ('The string "' + name + '" has ' + str(upper_count) + " upper case letters and " + str(lower_count) + " lower case letters.")
    print(counted)

case_count()

