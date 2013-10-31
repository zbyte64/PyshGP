'''
Created on Oct 26, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
from .. import pushstate

#instructions for booleans

def boolean_and(state):
    if len(state['boolean']>1):
        ret = pushstate.stack_ref('boolean', 0, state) and pushstate.stack_ref('boolean', 1, state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'boolean', state)
        return state
pushstate.define_registered('boolean_and', boolean_and)

def boolean_or(state):
    if len(state['boolean']>1):
        ret = pushstate.stack_ref('boolean', 0, state) or pushstate.stack_ref('boolean', 1, state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'boolean', state)
pushstate.define_registered('boolean_or', boolean_or)

def boolean_not(state):
    if len(state['boolean']>0):
        ret = not (pushstate.stack_ref('boolean', 0, state))
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'boolean', state)
pushstate.define_registered('boolean_not', boolean_not)

def boolean_xor(state):
    if len(state['boolean']>1):
        b1 = pushstate.stack_ref('boolean', 0, state)
        b2 = pushstate.stack_ref('boolean', 1, state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.pop_item('boolean', state)
        if not (b1 and b2) and (b1 or b2):
            state = pushstate.push_item(True, 'boolean', state)
        else:
            state = pushstate.push_item(False, 'boolean', state)
        return state
pushstate.define_registered('boolean_xor', boolean_xor)

def boolean_invert_first_then_and(state):
    if len(state['boolean']>1):
        ret = (not pushstate.stack_ref('boolean', 0, state)) and pushstate.stack_ref('boolean', 1, state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'boolean', state)
        return state
pushstate.define_registered('boolean_invert_first_then_and', boolean_invert_first_then_and)

def boolean_invert_second_then_and(state):
    if len(state['boolean']>1):
        ret = pushstate.stack_ref('boolean', 0, state) and (not pushstate.stack_ref('boolean', 1, state))
        state = pushstate.pop_item('boolean', state)
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'boolean', state)
        return state
pushstate.define_registered('boolean_invert_second_then_and', boolean_invert_second_then_and)

def boolean_frominteger(state):
    if len(state['integer']>1):
        ret = pushstate.stack_ref('integer', 0, state)
        if ret == 0:
            ret = False
        else:
            ret = True
        state = pushstate.pop_item('integer', state)
        state = pushstate.push_item(ret, 'boolean', state)
pushstate.define_registered('boolean_frominteger', boolean_frominteger)

def boolean_fromfloat(state):
    if len(state['float']>1):
        ret = pushstate.stack_ref('float', 0, state)
        if ret == 0.0:
            ret = False
        else:
            ret = True
        state = pushstate.pop_item('float', state)
        state = pushstate.push_item(ret, 'boolean', state)
pushstate.define_registered('boolean_fromfloat', boolean_fromfloat)