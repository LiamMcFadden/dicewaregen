#!/usr/bin/env python3


"""
   THis make randum numbres lol!
"""

import secrets
from sys import argv

pword = ''
n = 5 if len(argv) == 1 else int(argv[1])


for i in range(n):
    res = ''
    for j in range(5):
        res += str(secrets.randbelow(6)+1)
    
    with open('./diceware.list') as f:
        for line in f:
            if line.startswith(res):
                pword += f'{line.split()[1]} '

print(pword)
