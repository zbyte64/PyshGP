'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import globals
from .. import pushstate
from .. import util
from .. import random_push

def boolean_rand(state):
    return pushstate.push_item(random_push.lrand_nth([True, False]), 'boolean', state)
pushstate.define_registered('boolean_rand', boolean_rand)

def integer_rand(state):
    temp = globals.max_random_integer - globals.min_random_integer + 1
    temp = random_push.lrand_int(temp)+globals.min_random_integer
    return pushstate.push_item(temp, 'integer', state)
pushstate.define_registered('integer_rand', integer_rand)

def float_rand(state):
    temp = globals.max_random_float - globals.min_random_float
    temp = random_push.lrand(temp)+globals.min_random_float
    return pushstate.push_item(temp, 'float', state)
pushstate.define_registered('float_rand', float_rand)

def code_rand(state):
    if len(state['integer'])>0:
        if len(globals.global_atom_generators) == 0:
            print("code_rand: global-atom-generators is empty.")
        else:
            max_points = pushstate.stack_ref('integer', 0, state)
            max_points = abs(max_points % globals.max_points_in_random_expressions)
            if max_points < 1:
                max_points = 1
            state = pushstate.push_item(random_push.random_code(max_points, globals.global_atom_generators),
                                        'code',
                                        pushstate.pop_item('integer', state))
    return state
pushstate.define_registered('code_rand', code_rand)

def string_rand(state):
    ret = ''
    for i in range(random_push.lrand_int(globals.max_string_length-globals.min_random_string_length)):
        options = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        index = random_push.lrand_int(len(options))
        ret = ret + options[index]
    return pushstate.push_item(ret, 'string', state)
pushstate.define_registered('string_rand', string_rand)