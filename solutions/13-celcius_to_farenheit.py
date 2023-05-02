#!/usr/bin/env python3

temp = "Enter a value for °C or F to convert"
temp +="\n(enter 'q' to quit at any time): "
c_or_f = "Enter C or F to specify celsius or farenheit"
active = True
while active == True:
    value = input(temp)
    if value.lower() == 'q':
        break
    unit = input(c_or_f)
    if unit.lower() == 'q':
        break
    if unit.lower() == 'c':
        faren = ((int(value) * (9/5)) + 32)
        print(value + "°C is " + str(int(faren)) + " in Farenheit")
    if unit.lower() == 'f':
        cels = ((int(value) - 32) * (5/9))
        print(value + "°F is " + str(int(cels)) + " in Celsius")


