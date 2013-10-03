'''
Created on Oct 2, 2013

@author: Eddie
'''
import pyshGlobals
from stacks import Number_Instructions

class PyshState(object):
    '''
    classdocs
    '''
    stacks = {}

    def __init__(self):
        '''
        Constructor
        '''
        for typ in pyshGlobals.pysh_types:
            if (typ is int) or (typ is float):
                self.stacks[typ.__name__] = Number_Instructions()
            else:
                pass #FOR NOW

    def state_pretty_print(self):
        for i in self.stacks:
            temp = ", ".join(map(str, self.stacks[i].get_stack()))
            print i + ': ' + temp
            
    def push_item(self, val, typ):
        '''
        Value pushed on the named stack. This is a utility, not for use in Push programs.
        '''
        self.stacks[typ].stack.append(val)
        
    def top_item(self, typ):
        '''
         Returns the top item of the type stack in state. Returns None if called on
        an empty stack. This is a utility, not for use as an instruction in Push programs.
        '''
        if len(self.stacks[typ].get_stack()) != 0:
            return self.stacks[typ].get_stack()[len(self.stacks[typ].get_stack())-1]
        else:
            return None
    
    def stack_ref(self, typ):
        '''
        Returns the indicated item of the type stack in state. Returns None if called
        on an empty stack. This is a utility, not for use as an instruction in Push programs.
        NOT SAFE for invalid positions.
        '''
        if len(self.stacks[typ]) != 0:
            return self.stacks[typ].pop()
        else:
            return None
        
    def pop_item(self, typ):
        '''
         Returns, and removes, the top item of the type stack in state. Returns None if called on
        an empty stack. This is a utility, not for use as an instruction in Push programs.
        '''
        if len(self.stacks[typ].get_stack()) != 0:
            return self.stacks[typ].get_stack().pop()
        else:
            return None
        
    
g = PyshState()
g.push_item(5, 'int')
g.push_item(2.5, 'float')
g.push_item(75, 'int')
g.state_pretty_print()
print
g.pop_item('int')
g.state_pretty_print()