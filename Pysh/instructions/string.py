'''
Created on Nov 8, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
from .. import pushstate
from .. import util
from .. import globals
import re

def string_concat(state):
    if len(state['string'])>1:
        s1 = pushstate.stack_ref('string', 0, state)
        s2 = pushstate.stack_ref('string', 1, state)
        state = pushstate.pop_item('string', state)
        state = pushstate.pop_item('string', state)
        state = pushstate.push_item(s1+s2, 'string', state)
        return state
pushstate.define_registered('string_concat', string_concat)

def string_take(state):
    if len(state['string']>0 and len(state['integer']>0)):
        s1 = pushstate.stack_ref('string', 0, state)
        int1 = pushstate.stack_ref('integer', 0, state)
        state = pushstate.pop_item('string', state)
        state = pushstate.pop_item('integer', state)
        state = pushstate.push_item(s1[:int1], 'string', state)
        return state
pushstate.define_registered('string_take', string_take)

def string_length(state):
    if len(state['string'])>0:
        s1 = pushstate.stack_ref('string', 0, state)
        state = pushstate.pop_item('string', state)
        state = pushstate.push_item(len(s1), 'integer', state)
        return state
pushstate.define_registered('string_length', string_length)

p = re.compile(r'[^\d-]*(-?[\d]+(\.[\d]*)?([eE][+-]?[\d]+)?)')
def string_atoi(state):
    if len(state['string'])>0:
        s1 = pushstate.stack_ref('string', 0, state)
        state = pushstate.pop_item('string', state)
        m = p.match(s1)
        if m:
            result = m.groups()[0]
            if "." in result or "e" in result or "E" in result:
                ret = "{1}".format(s1, float(result))
                state = pushstate.push_item(ret, 'float', state)
            else:
                ret = '{1}'.format(s1, int(result))
                state = pushstate.push_item(ret, 'integer', state)
        return state
pushstate.define_registered('string_atoi', string_length)

def string_reverse(state):
    if len(state['string'])>0:
        s1 = pushstate.stack_ref('string', 0, state)
        state = pushstate.pop_item('string', state)
        def reverse(text):
            if len(text) <= 1:
                return text
            return reverse(text[1:]) + text[0]
        state = pushstate.push_item(reverse(s1), 'string', state)
        return state
pushstate.define_registered('string_reverse', string_reverse)

def string_parse_to_chars(state):
    if len(state['string'])>0:
        s1 = pushstate.stack_ref('string', 0, state)
        state = pushstate.pop_item('string', state)
        for i in range(len(s1-1)):
            state = pushstate.push_item(s1[len(s1)-i:], 'string', state)
        return state
pushstate.define_registered('string_parse_to_chars', string_parse_to_chars)

def string_contained(state):
    if len(state['string'])>0:
        s1 = pushstate.stack_ref('string', 0, state)
        s2 = pushstate.stack_ref('string', 1, state)
        state = pushstate.pop_item('string', state)
        state = pushstate.pop_item('string', state)
        if s1 in s2:
            state = pushstate.push_item(True, 'boolean', state)
        else:
            state = pushstate.push_item(False, 'boolean', state)
        return state
pushstate.define_registered('string_contained', string_contained)