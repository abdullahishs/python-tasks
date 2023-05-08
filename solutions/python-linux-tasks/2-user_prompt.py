#!/usr/bin/env python3

import os
from random import randrange as rnd

x = (rnd(1,20))
y = (rnd(1,20))

user_answer = input(f"What is {x} x {y}: ")

try: 
    int(user_answer)
except ValueError:
    os.system(f"echo 'You need to enter a number'")
    quit()

if int(user_answer) ==  (x*y):
    os.system("echo 'That is the correct answer. Well Done!!'")
elif int(user_answer) == (""):
    os.system("echo 'You never entered anything, given up??'")
else:
    os.system(f"echo 'Incorrect, the correct answer is {x*y}'")