#!/usr/bin/env python3

import os

os.system("useradd -s /bin/bash python-user")
os.system("sudo passwd python-user")
#os.system("su python-user")