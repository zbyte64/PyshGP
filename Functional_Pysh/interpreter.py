'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College
'''

def execute_instruction(instruction, state):
    '''
    Execute a single Push instruction
    '''
    if instruction == None:
        return state
    else:
        