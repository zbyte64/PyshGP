'''
Created on Oct 2, 2013

@author: Eddie
'''
import random

class Exec(object):
    symbol = None
    def __init__(self, sym):
        self.symbol = sym

def rand(typ, min = None, max = None):
    if typ == int:
        return random.randint(min, max)
    elif typ is Exec:
        print('Hit')
        line = random.choice(open('PyshInstructionsList.txt').readlines())
        if line[:1] == '#':
            return rand(Exec)
        else:
            return line
        
pysh_types = [int, float, Exec]