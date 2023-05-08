#!/usr/bin/env python3

def rps_game():
    player_1 = "Player 1, Make your choice: "
    player_2 = "Player 2, Make your choice: "
    new = "Do you want to start a new game? (enter 'n' to quit): "
    valid_choices = ["rock", "paper", "scissors"]
    active = True
    while active == True:
        x = input(player_1)
        if x == 'q':
            break
        elif x.lower() not in valid_choices:
            print(f"{x} is not a valid choice")
            break
        y = input(player_2)
        if y == 'q':
            break
        elif y.lower() not in valid_choices:
            print(f"{y} is not a valid choice")
            break
        if x.lower() == y.lower():
            print ("Its a DRAW\nTry Again")
        if x.lower() == 'rock' and y.lower() == 'paper':
            print ("Player 2 Wins!")
            if input(new.lower()) == 'n':
                break
            else:
                continue
        elif x.lower() == 'rock' and y.lower() == 'scissors':
            print ("Player 1 Wins!")
            if input(new.lower()) == 'n':
                break
            else:
                continue
        elif x.lower() == 'paper' and y.lower() == 'rock':
            print ("Player 1 Wins!")
            if input(new.lower()) == 'n':
                break
            else:
                continue
        elif x.lower() == 'paper' and y.lower() == 'scissors':
            print ("Player 2 Wins!")
            if input(new.lower()) == 'n':
                break
            else:
                continue
        elif x.lower() == 'scissors' and y.lower() == 'paper':
            print ("Player 1 Wins!")
            if input(new.lower()) == 'n':
                break
            else:
                continue
        elif x.lower() == 'scissors' and y.lower() == 'rock':
            print ("Player 2 Wins!")
            if input(new.lower()) == 'n':
                break
            else:
                continue

rps_game()
        
