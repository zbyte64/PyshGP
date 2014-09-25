'''
Created on Oct 23, 2013

All functions are taken straing from lspector's Clojush project

@author: Eddie Pantridge Hampshire College 2013
'''
import globals

def make_push_state():
    '''
    returns empty push state
    '''
    state = {}
    for t in globals.push_types:
        state[t] = []
    return state

registered_instructions = []
def register_instruction(name):
    '''
    Add the provided name to the global list of registered instructions.
    '''
    if registered_instructions.count(name)>0:
        print('Duplicate Push instruction defined: ' + name)
    else:
        registered_instructions.append(name)
    
instruction_table = {}
def define_registered(instruction, definition):
    register_instruction(instruction)
    instruction_table[instruction] = definition
    
def get_instruction_table():
    return instruction_table
    
def state_pretty_print(state):
    for t in state.keys():
        line = t + ': '
        for i in state[t]:
            line += str(i) + ", "
        print line

def push_item(value, push_type, state):
    '''
    Returns a copy of the state with the value pushed on the named stack. This is a utility,
    not for use in Push programs.
    '''
    state[push_type].insert(0,value)
    return state

def top_item(type, state):
    '''
    Returns the top item of the type stack in state. 
    This is a utility, not for use as an instruction in Push programs.
    '''
    stack = state[type]
    if len(stack)>0:
        return stack[0]
    else:
        return "NO-STACK-ITEM"
    
def stack_ref(type, position, state):
    '''
    Returns the indicated item of the type stack in state.
    This is a utility, not for use as an instruction in Push programs.
    NOT SAFE for invalid positions.
    '''
    stack = state[type]
    if len(stack)>0:
        return stack[position]
    else:
        print "NO-STACK-ITEM"

def pop_item(type, state):
    '''
    Returns a copy of the state with the specified stack popped. This is a utility,
    not for use as an instruction in Push programs.
    '''
    #for t in state.keys():
    #    print str(state[t])
    try:
        state[type] = state[type][1:]
    except IndexError: 
        print "POP FROM EMPTY " + type + " LIST"
    return state

def end_environment(state):
    '''
    Ends the current environment by popping the 'environment' stack and replacing
    all stacks with those on the environment stack. Then, everything on the old
    'return' stack is pushed onto the 'exec' stack.
    '''
    new_env = top_item('environment', state)
    new_exec = state['exec'] + new_env['exec']
    
    old_return = state['return']
    new_state = new_env
    new_state['exec'] = new_exec
    new_state['auxiliary'] = state['auxiliary']
    while len(old_return>0):
        old_return.pop(0)
        new_state = push_item(old_return[0], 'exec', new_state)
    return new_state

def registered_nonrandom():
    '''
    Returns a list of all registered instructions aside from random instructions.
    '''
    ret = []
    for i in registered_instructions:
        if not i.endswith('_rand'):
            ret.append(i)
    return ret