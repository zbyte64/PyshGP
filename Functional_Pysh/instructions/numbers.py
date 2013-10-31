'''
Created on Oct 29, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import pushstate
from .. import util

def adder(type):
    '''
    Returns a function that pushes the sum of the top two items.
    '''
    def add(state):
        if len(state[type]>1):
            ret = pushstate.stack_ref(type, 0, state) + pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
    return add
pushstate.define_registered('integer_add', adder('integer'))
pushstate.define_registered('float_add', adder('float'))

def subtracter(type):
    '''
    Returns a function that pushes the difference of the top two items.
    '''
    def sub(state):
        if len(state[type]>1):
            ret = pushstate.stack_ref(type, 0, state) - pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
    return sub
pushstate.define_registered('integer_sub', subtracter('integer'))
pushstate.define_registered('float_sub', subtracter('float'))

def multiplier(type):
    '''
    Returns a function that pushes the product of the top two items.
    '''
    def mult(state):
        if len(state[type]>1):
            ret = pushstate.stack_ref(type, 0, state) * pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
    return mult
pushstate.define_registered('integer_mult', multiplier('integer'))
pushstate.define_registered('float_mult', multiplier('float'))

def divider(type):
    '''
    Returns a function that pushes the quotient of the top two items.
    Does nothing if the denominator would be zero.
    '''
    def div(state):
        if len(state[type]>1):
            if pushstate.stack_ref(type, 1, state) != 0:
                ret = pushstate.stack_ref(type, 0, state) / pushstate.stack_ref(type, 1, state)
                ret = util.keep_number_reasonable(ret)
                state = pushstate.pop_item(type, state)
                state = pushstate.pop_item(type, state)
                state = pushstate.push_item(ret, type, state)
    return div
pushstate.define_registered('integer_div', divider('integer'))
pushstate.define_registered('float_div', divider('float'))

def modder(type):
    '''
    Returns a function that pushes the modulus of the top two items.
    Does nothing if the denominator would be zero.
    '''
    def mod(state):
        if len(state[type]>1):
            ret = pushstate.stack_ref(type, 0, state) % pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
    return mod
pushstate.define_registered('integer_mod', modder('integer'))
pushstate.define_registered('float_mod', modder('float'))

def lessthaner(type):
    '''
    Returns a function that pushes the result of < of the top two items onto the boolean stack.
    '''
    def lt(state):
        if len(state[type]>1):
            ret = pushstate.stack_ref(type, 0, state) < pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, 'boolean', state)
    return lt
pushstate.define_registered('integer_lt', lessthaner('integer'))
pushstate.define_registered('float_lt', lessthaner('float'))

def greaterthaner(type):
    '''
    Returns a function that pushes the result of < of the top two items onto the boolean stack.
    '''
    def gt(state):
        if len(state[type]>1):
            ret = pushstate.stack_ref(type, 0, state) > pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, 'boolean', state)
    return gt
pushstate.define_registered('integer_gt', greaterthaner('integer'))
pushstate.define_registered('float_gt', greaterthaner('float'))