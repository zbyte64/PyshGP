'''
Created on Nov 12, 2013

@author: Eddie Pantirdge Hampsshire College 2013
'''
from .. import pushstate

def returner(type):
    '''
    Returns a function that takes a state and moves the top literal
    from the appropriate stack to the return stack.
    '''
    def ret(state):
        if len(state[type]) == 0:
            return state
        else:
            item = pushstate.top_item(type, state)
            return pushstate.push_item(item, 'return', (pushstate.pop_item(type, state)))
    return ret
pushstate.define_registered('return_fromexec', returner('exec'))
pushstate.define_registered('return_frominteger', returner('integer'))
pushstate.define_registered('return_fromfloat', returner('float'))
pushstate.define_registered('return_fromboolean', returner('boolean'))
pushstate.define_registered('return_fromstring', returner('string'))

def return_fromcode(state):
    if len(state['code'])==0:
        return state
    else:
        item = ['code_quote', pushstate.top_item('code', state)]
        return pushstate.push_item(item, 'return', pushstate.pop_item('code', state))
pushstate.define_registered('return_fromcode', return_fromcode)

def return_exec_pop(state):
    state['return'].append('exec_pop')
    return state
pushstate.define_registered('return_exec_pop', return_exec_pop)

def return_code_pop(state):
    state['return'].append('code_pop')
    return state
pushstate.define_registered('return_code_pop', return_code_pop)

def return_integer_pop(state):
    state['return'].append('integer_pop')
    return state
pushstate.define_registered('return_integer_pop', return_integer_pop)

def return_float_pop(state):
    state['return'].append('float_pop')
    return state
pushstate.define_registered('return_float_pop', return_float_pop)

def return_boolean_pop(state):
    state['return'].append('boolean_pop')
    return state
pushstate.define_registered('return_boolean_pop', return_boolean_pop)

def return_zip_pop(state):
    state['return'].append('zip_pop')
    return state
pushstate.define_registered('return_zip_pop', return_zip_pop)

def return_string_pop(state):
    state['return'].append('string_pop')
    return state
pushstate.define_registered('return_string_pop', return_string_pop)

#Immediately copies the current tagspace to the environment on the top of the :environment stack.
def return_tagspace(state):
    if len(state['environment'])==0:
        return state
    else:
        top_env = (pushstate.top_item('environment', state))
        new_env = state
        state = pushstate.pop_item('environment', new_env) 
        return pushstate.push_item(new_env, 'environment', state)
pushstate.define_registered('return_tagspace', return_tagspace)