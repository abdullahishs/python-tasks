#!/usr/bin/env python3

lists = []
for x in range(100,401):
    active = True
    for y in str(x):
        if int(y) % 2 != 0:
            active = False
    if active == True:
        lists.append(x)
print (lists)
