'''
Created on Oct 2, 2013

@author: Eddie
'''
import random

def rand(typ, min = None, max = None):
    if typ == int:
        return random.randint(min, max)
    elif type == float:
        return random.uniform(min, max)
    elif typ == "Exec":
        line = random.choice(open('PyshInstructionsList.txt').readlines())
        if line[:1] == '#':
            return rand("Exec")
        else:
            return line[:len(line)-1]
        
pysh_types = [int, float, "Exec"]