#!/usr/bin/env python3

chosen_meat = "Press '1' for Beef, '2' for Chicken, '3' for Lamb and '4' for Pork: "
chosen_weight = "How many kg of meat will you require: "
active = True
while active == True:
    meat = input(chosen_meat)
    kg = input(chosen_weight)
    if meat == '1':
        print ("You have chosen " + kg + "kg of Beef\n")
        print ("This will take " + str(int((50*float(kg))+20)) + "mins to cook")
    if meat == '2':
        print ("You have chosen " + kg + "kg of Chicken\n")
        print ("This will take " + str(int((45*float(kg))+20)) + "mins to cook")
    if meat == '3':
        print ("You have chosen " + kg + "kg of Lamb")
        print ("This will take " + str(int((60*float(kg))+30)) + "mins to cook")
    if meat == '4':
        print ("You have chosen " + kg + "kg of Pork")
        print ("This will take " + str(int((70*float(kg))+35)) + "mins to cook")  

