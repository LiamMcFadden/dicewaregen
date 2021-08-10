#!/usr/bin/env python
# this is a bad practice but my python install is messed up and I don't wanna fix it


"""
   THis make randum numbres lol!
"""

import secrets

pword = ''

for i in range(5):
    res = ''
    for j in range(5):
        res += str(secrets.randbelow(6)+1)
    
    with open('./diceware.list') as f:
        for line in f:
            if line.startswith(res):
                pword += f'{line.split()[1]} '

print(pword)
