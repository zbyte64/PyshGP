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
        if len(state[type])>1:
            ret = pushstate.stack_ref(type, 0, state) + pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
            print("THIS SHOULD HIT!")
            return state
    return add
pushstate.define_registered('integer_add', adder('integer'))
pushstate.define_registered('float_add', adder('float'))

def subtracter(type):
    '''
    Returns a function that pushes the difference of the top two items.
    '''
    def sub(state):
        if len(state[type])>1:
            ret = pushstate.stack_ref(type, 0, state) - pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
            return state
    return sub
pushstate.define_registered('integer_sub', subtracter('integer'))
pushstate.define_registered('float_sub', subtracter('float'))

def multiplier(type):
    '''
    Returns a function that pushes the product of the top two items.
    '''
    def mult(state):
        if len(state[type])>1:
            ret = pushstate.stack_ref(type, 0, state) * pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
            return state
    return mult
pushstate.define_registered('integer_mult', multiplier('integer'))
pushstate.define_registered('float_mult', multiplier('float'))

def divider(type):
    '''
    Returns a function that pushes the quotient of the top two items.
    Does nothing if the denominator would be zero.
    '''
    def div(state):
        if len(state[type])>1:
            if pushstate.stack_ref(type, 1, state) != 0:
                ret = pushstate.stack_ref(type, 0, state) / pushstate.stack_ref(type, 1, state)
                ret = util.keep_number_reasonable(ret)
                state = pushstate.pop_item(type, state)
                state = pushstate.pop_item(type, state)
                state = pushstate.push_item(ret, type, state)
                return state
    return div
pushstate.define_registered('integer_div', divider('integer'))
pushstate.define_registered('float_div', divider('float'))

def modder(type):
    '''
    Returns a function that pushes the modulus of the top two items.
    Does nothing if the denominator would be zero.
    '''
    def mod(state):
        if len(state[type])>1:
            ret = pushstate.stack_ref(type, 0, state) % pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, type, state)
            return state
    return mod
pushstate.define_registered('integer_mod', modder('integer'))
pushstate.define_registered('float_mod', modder('float'))

def lessthaner(type):
    '''
    Returns a function that pushes the result of < of the top two items onto the boolean stack.
    '''
    def lt(state):
        if len(state[type])>1:
            ret = pushstate.stack_ref(type, 0, state) < pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, 'boolean', state)
            return state
    return lt
pushstate.define_registered('integer_lt', lessthaner('integer'))
pushstate.define_registered('float_lt', lessthaner('float'))

def greaterthaner(type):
    '''
    Returns a function that pushes the result of < of the top two items onto the boolean stack.
    '''
    def gt(state):
        if len(state[type])>1:
            ret = pushstate.stack_ref(type, 0, state) > pushstate.stack_ref(type, 1, state)
            ret = util.keep_number_reasonable(ret)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.push_item(ret, 'boolean', state)
            return state
    return gt
pushstate.define_registered('integer_gt', greaterthaner('integer'))
pushstate.define_registered('float_gt', greaterthaner('float'))

def integer_fromboolean(state):
    if len(state['boolean'])>0:
        ret = pushstate.stack_ref('boolean', 0, state)
        if ret:
            ret = 1
        else:
            ret = 0
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'integer', state)
        return state
pushstate.define_registered('integer_fromboolean', integer_fromboolean)

def float_fromboolean(state):
    if len(state['boolean'])>0:
        ret = pushstate.stack_ref('boolean', 0, state)
        if ret:
            ret = 1.0
        else:
            ret = 0.0
        state = pushstate.pop_item('boolean', state)
        state = pushstate.push_item(ret, 'float', state)
        return state
pushstate.define_registered('float_fromboolean', float_fromboolean)

def integer_fromfloat(state):
    if len(state['float'])>0:
        ret = pushstate.stack_ref('float', 0, state)
        ret = int(ret)
        state = pushstate.pop_item('float', state)
        state = pushstate.push_item(ret, 'integer', state)
        return state
pushstate.define_registered('integer_fromfloat', integer_fromfloat)

def float_frominteger(state):
    if len(state['float'])>0:
        ret = pushstate.stack_ref('integer', 0, state)
        ret = int(ret)
        state = pushstate.pop_item('integer', state)
        state = pushstate.push_item(ret, 'float', state)
        return state
pushstate.define_registered('float_frominteger', float_frominteger)

def minner(type):
    '''
    Returns a function that pushes the minimum of the top two items.
    '''
    def min(state):
        if len(state[type])>0:
            num1 = pushstate.stack_ref(type, 0, state)
            num2 = pushstate.stack_ref(type, 1, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            if num1 > num2:
                state = pushstate.push_item(num2, type, state)
            else:
                state = pushstate.push_item(num1, type, state)
            return state
    return min
pushstate.define_registered('integer_min', minner('integer'))
pushstate.define_registered('float_min', minner('float'))

def maxer(type):
    '''
    Returns a function that pushes the maximum of the top two items.
    '''
    def max(state):
        if len(state[type])>0:
            num1 = pushstate.stack_ref(type, 0, state)
            num2 = pushstate.stack_ref(type, 1, state)
            state = pushstate.pop_item(type, state)
            state = pushstate.pop_item(type, state)
            if num1 > num2:
                state = pushstate.push_item(num1, type, state)
            else:
                state = pushstate.push_item(num2, type, state)
            return state
    return max
pushstate.define_registered('integer_max', maxer('integer'))
pushstate.define_registered('float_max', maxer('float'))

#what exactly does the Sin, Cos, and Tanget functions do?
#Will be added later