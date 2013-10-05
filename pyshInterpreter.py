'''
Created on Oct 2, 2013

@author: Eddie
'''
import pyshState
import pyshGlobals
import random

from pyshGlobals import Exec

class PyshInterpreter(object):
    '''
    classdocs
    '''
    state = None

    def __init__(self):
        '''
        Constructor
        '''
        self.state = pyshState.PyshState()
        self.state.push_item(1, 'int') 
        self.state.push_item(2, 'int')       
        self.state.push_item(pyshGlobals.rand(Exec), 'Exec')
        self.state.state_pretty_print()
        self.temp_step()
        
    def temp_step(self):
        #self.state.push_item(random.randint(1, 10), 'int')
        #self.state.push_item(pyshGlobals.rand(Exec), 'Exec')
        
        #print(self.state.top_item('Exec'))
        #print(self.state.top_item('int'))
        #print
        
        self.temp_exec()
        
    def temp_exec(self):
        ex = self.state.pop_item('Exec')
        if ex[:3] == '$ni':
            print(ex[3:])
            if ex[3:] == 'a':
                self.state.stacks['int'].adder()
            elif ex[3:] == 's':
                self.state.stacks['int'].subtracter()
            elif ex[3:] == 'm':
                self.state.stacks['int'].multiplier()
            elif ex[3:] == 'd':
                self.state.stacks['int'].divider()
            elif ex[3:] == 'md':
                self.state.stacks['int'].modder()
            elif ex[3:] == 'min':
                self.state.stacks['int'].minner()
            elif ex[3:] == 'max':
                self.state.stacks['int'].maxer()
            else:
                print('No Nunmber Instruction with Symbol: ' + ex)
        else:
            print('Non-number types Not Implemented Yet!')
        
pi = PyshInterpreter()