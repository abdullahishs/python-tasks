#!/usr/bin/env python3

'''5. Create a program to add the user created in the previous exercise to the wheel group. 
Test that the user can now use sudo.'''

import os

os.system("usermod -aG sudo python-user")
#os.system("su python-user")
#os.system("sudo ls /")