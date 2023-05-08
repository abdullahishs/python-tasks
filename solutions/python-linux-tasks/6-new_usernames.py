#!/usr/bin/env python3

from os import system as linux

for x in range(1,6):
    linux(f"echo 'user-{x}' >> ../../../../names.txt")

