#!/usr/bin/env python3

import os

usernames = open('names.txt', 'r')
users = usernames.readlines()

for line in users:
    print(f"Creating user: '{line.strip()}'...")
    os.system(f"useradd -s /bin/bash {line.strip()}")
    #os.system(f"passwd -d {line.strip()}")

print("User creation complete!")
usernames.close()

