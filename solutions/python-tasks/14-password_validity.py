#!/usr/bin/env python3

import re

password = input("Enter your password and I will validate it for you: ")
invalid = 0

if len(password) < 6:
    print("Your password is too short")
    quit()
elif len(password) > 16:
    print("Your password is too long")
    quit()

if re.search('[!@#$%^&*_<>/]', password):
    password = password
else:
    invalid += 1
    print("You need to include one of the following special characters - !@#$%^&*_<>/")

if re.search('[A-Z]', password):
    password = password
else:
    invalid += 1
    print("Your password needs to include an upper case letter")

if re.search('[a-z]', password):
    password = password
else:
    invalid += 1
    print("Your password needs to include a lower case letter")

if re.search('[0-9]', password):
    password = password
else:
    invalid += 1
    print("Your password needs to include a number")

if invalid > 0:
    print("Invalid Password")
else:
    print("Your password is valid")



