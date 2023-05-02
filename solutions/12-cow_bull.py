#!/usr/bin/env python3

print('''The aim of this game is to guess a random 4 digit number. 
For each guess you make the game will tell you the corresponding 'Cow' or 'Bull' number. 
A 'Cow' mean that you have a correct digit in the right place, and a 'Bull' means you have a correct digit but in the wrong place. 
Each digit only appears once and there are no repeating digits.
The game ends once you have cracked the code, but you only have 10 attempts to crack it. Good Luck!''')

def cow_bull():
    import random
    digits = list(range(10))
    random.shuffle(digits)
    n = ''.join(map(str, digits[:4]))
    if str(n[0]) == '0':
        cow_bull
    tries = 10
    while True:
        g = input("Guess a number: ")
        incor = 0
        four_digits = 0
        cow = 0
        bull = 0
        repeating = 0
        tries -= 1


        if g.lower() == 'quit' or g.lower() == 'q':
            quit()

        if len(g) == len(set(g)):
            g = g
        else:
            repeating += 1
            print("Your guess should not have repeating digits")
            
        for x in g:
            four_digits += 1
            try:
                int(x)
            except ValueError:
                incor += 1
        if incor > 0:
            print (f"You have entered an incorrect value: {g}")

        if four_digits == 4:
            for i in range(4):
                if g[i] == n[i]:
                    cow += 1
                elif g[i] in n:
                    bull += 1
        else:
            print("You can only enter 4 digits")
        

        if cow == 4:
            print ("Congratulations, You cracked the code!")
            new_game = input("Do you want to play again? (Press 'q' to quit, or ENTER to play again): ")
            if new_game == "q":
                quit()
            else:
                cow_bull()

        if incor == 0 and four_digits == 4 and repeating == 0:
            print("cow:",cow)
            print("bull:",bull)
        

        if tries == 1:
            print (f"Only {tries} attempt remaining.")
        elif tries == 0:
            print (f"Unlucky, you have run out of attempts. The code was {n}")
            new_game = input("Do you want to play again? (Press 'q' to quit, or ENTER to play again): ")
            if new_game == "q":
                quit()
            else:
                cow_bull()
        else:        
            print (f"{tries} attempts remaining.")
        


        #print(n)
        #print(g)

cow_bull()
