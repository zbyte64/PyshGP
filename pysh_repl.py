'''
Created on Sep 24, 2013

@author: Eddie
'''
import re
from Pysh import PyshController

class Pysh_Repl(object):
    '''
    classdocs
    '''
    pc = None

    def __init__(self):
        '''
        Constructor
        '''
        print "Pysh REPL Starting"
        self.pc = PyshController()
        self.step()
        
    def step(self):
        read = raw_input()
        
        paramInd = []
        params = []
        for i in re.finditer( ' ', read ):
            paramInd.append(i.end())
        count = 0
        for i in paramInd:
            if count < len(paramInd)-1:
                params.append(read[i:i+1])
            else:
                params.append(read[i:])
            count += 1
            
        #print(params)
            
        if read[:4] == 'push':
            self.pc.push(params[0], params[1])
            
        elif read[:3] == 'pop':
            self.pc.pop(params[0])
            print('Popping')
            
        elif read[:3] ==  'add':
            self.pc.add(params[0], params[1])
            
        elif read[:8] ==  'subtract':
            self.pc.subtract(params[0], params[1])
            
        elif read[:8] ==  'multiply':
            self.pc.multiply(params[0], params[1])
        
        elif read[:6] ==  'divide':
            self.pc.divide(params[0], params[1])
        
        elif read[:9] == 'print_all':
            self.pc.print_all_stacks()
            
        elif read[:5] == 'print':
            self.pc.print_stack(params[0])
        
        if read != "exit":
            self.step()
        else:
            print("Exiting REPL")

pcr = Pysh_Repl()