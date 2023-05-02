#!/usr/bin/env python3

def random_game():
    from random import randrange as rnd
    x =  (rnd(1,10))
    user_guess = "Pick a number from 1 to 9: "
    active = True
    while active == True:
        user = input(user_guess)
        if int(user) == x:
            print("Well Guessed!")
            break
        else:
            print ("Try again")

random_game()



