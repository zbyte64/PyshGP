'''
Created on Oct 2, 2013

@author: Eddie
'''
import random

class Exec(list):
    def __init__(self, l):
        for i in range(len(l)):
            self.append(l[i])

def rand(typ, min = None, max = None):
    '''
    Not used anymore. Ignore this function
    '''
    if typ == int:
        return random.randint(min, max)
    elif type == float:
        return random.uniform(min, max)
    elif typ == "Exec":
        #NOT REALLY MEANT TO BE USED. EXECS SHOULD BE READ FROM PUSH PROGRAM
        line = random.choice(open('PyshInstructionsList.txt').readlines())
        if line[:1] == '#':
            return rand("Exec")
        else:
            return line[:len(line)-1]
        
pysh_types = [int, float, Exec]

'''
#Testing Type Exec
e = Exec([1, 0, 5])
print e
'''