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

    def __init__(self):
        '''
        Constructor
        '''
        self.state = pyshState.PyshState()
        
        #test fucntion
        self.state.push_item(['INTEGER.*', 'INTEGER.STACKDEPTH', 'CODE.DO*RANGE', 'INTEGER.MAX'], "Exec")
        self.state.state_pretty_print()
        
    def execute_instruction(self, instruction):
        print('Will evaluate: ' + instruction)
        print('Will then push result to correct stack')
        print
        
    def eval_push(self):
        '''
        Executes the contents of the exec stack.
        '''
        if len(self.state.stacks['Exec']) == 0:
            print('Exec Stack Empty')
        else:
            top_exec = self.state.pop_item('Exec')
            if type(top_exec) == list and len(top_exec) > 1:
                #is list reversal needed? I think yes
                rev_exec = []
                for i in reversed(top_exec):
                    rev_exec.append(i)
                for i in rev_exec:
                    self.state.push_item(i, 'Exec')
#                for i in top_exec:
#                    self.state.push_item(i, 'Exec')
            else:
                self.execute_instruction(top_exec)
        
                
pi = PyshInterpreter()
pi.eval_push()
pi.eval_push()
pi.eval_push()
pi.eval_push()
pi.eval_push()
pi.eval_push()