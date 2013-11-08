'''
Created on Nov 8, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
from .. import pushstate
from .. import util
from .. import globals

def string_concat(state):
    if len(state['string']>1):
        s1 = pushstate.stack_ref('string', 0, state)
        s2 = pushstate.stack_ref('string', 1, state)
        state = pushstate.pop_item('string', state)
        state = pushstate.pop_item('string', state)
        state = pushstate.push_item(s1+s2, 'string', state)
        return state
pushstate.define_registered('string_concat', string_concat)

def string_take(state):
    if len(state['string']>0 and len(state['integer']>0)):
        s1 = pushstate.stackref('string', 0, state)
        int1 = pushstate.stackref('integer', 0, state)
        state = pushstate.pop_item('string', state)
        state = pushstate.pop_item('integer', state)
        state = pushstate.push_item(s1[:int1], 'string', state)
        return state
pushstate.define_registered('string_take', string_take)