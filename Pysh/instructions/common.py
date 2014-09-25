'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import pushstate

#################################################################################
## Lookup function to see how many paren groups a function requires. Uses metadata.
def lookup_instruction_paren_groups(ins):
    pass


###############################################################################################
## instructions for all types (except non-data stacks such as auxiliary, tag, input, and output)
def popper(type):
    '''
    Returns a function that takes a state and pops the appropriate stack of the state.
    '''
    def pop(state):
        return pushstate.pop_item(type, state)
    return pop
pushstate.define_registered('exec_pop', popper('exec'))
pushstate.define_registered('integer_pop', popper('integer'))
pushstate.define_registered('float_pop', popper('float'))
pushstate.define_registered('code_pop', popper('code'))
pushstate.define_registered('boolean_pop', popper('boolean'))
pushstate.define_registered('string_pop', popper('string'))

def duper(type):
    '''
    Returns a function that takes a state and duplicates the top item of the appropriate
    stack of the state.
    '''
    def dup(state):
        if len(state[type])>0:
            state = pushstate.push_item(pushstate.top_item(type, state), type, state)
        return state
    return dup
pushstate.define_registered('exec_dup', duper('exec'))
pushstate.define_registered('integer_dup', duper('integer'))
pushstate.define_registered('float_dup', duper('float'))
pushstate.define_registered('code_dup', duper('code'))
pushstate.define_registered('boolean_dup', duper('boolean'))
pushstate.define_registered('string_dup', duper('string'))

def swapper(type):
    '''
    Returns a function that takes a state and swaps the top 2 items of the appropriate
    stack of the state.
    '''
    def swap(state):
        if len(state[type])>1:
            first_item = pushstate.stack_ref(type, 0, state)
            second_item = pushstate.stack_ref(type, 1, state)
            state = pushstate.pop_item(type, pushstate.pop_item(type, state))
            state = pushstate.push_item(first_item, type, state)
            state = pushstate.push_item(second_item, type, state)
        return state
    return swap
pushstate.define_registered('exec_swap', swapper('exec'))
pushstate.define_registered('integer_swap', swapper('integer'))
pushstate.define_registered('float_swap', swapper('float'))
pushstate.define_registered('code_swap', swapper('code'))
pushstate.define_registered('boolean_swap', swapper('boolean'))
pushstate.define_registered('string_swap', swapper('string'))

def rotter(type):
    '''
    Returns a function that takes a state and rotates the top 3 items of the appropriate
    stack of the state.
    '''
    def rotate(state):
        if len(state[type])>2:
            first = pushstate.stack_ref(type, 0, state)
            second = pushstate.stack_ref(type, 1, state)
            third = pushstate.stack_ref(type, 2, state)
            state = pushstate.pop_item(type, pushstate.pop_item(type, pushstate.pop_item(type, state)))
            state = pushstate.push_item(second, type, state)
            state = pushstate.push_item(first, type, state)
            state = pushstate.push_item(third, type, state)
        return state
    return rotate
pushstate.define_registered('exec_rot', rotter('exec'))
pushstate.define_registered('integer_rot', rotter('integer'))
pushstate.define_registered('float_rot', rotter('float'))
pushstate.define_registered('code_rot', rotter('code'))
pushstate.define_registered('boolean_rot', rotter('boolean'))
pushstate.define_registered('string_rot', rotter('string'))

def flusher(type):
    '''
    Returns a function that empties the stack of the given state.
    '''
    def flush(state):
        state[type] = []
        return state
    return flush
pushstate.define_registered('exec_flush', flusher('exec'))
pushstate.define_registered('integer_flush', flusher('integer'))
pushstate.define_registered('float_flush', flusher('float'))
pushstate.define_registered('code_flush', flusher('code'))
pushstate.define_registered('boolean_flush', flusher('boolean'))
pushstate.define_registered('string_flush', flusher('string'))

def eqer(type):
    '''
    Returns a function that compares the top two items of the appropriate stack of
    the given state.
    '''
    def eq(state):
        if len(state[type])>1:
            first = pushstate.stack_ref(type, 0, state)
            second = pushstate.stack_ref(type, 1, state)
            state = pushstate.pop_item(type, pushstate.pop_item(type, state))
            state = pushstate.push_item((first == second), 'boolean', state)
        return state
    return eq
pushstate.define_registered('exec_eq', eqer('exec'))
pushstate.define_registered('integer_eq', eqer('integer'))
pushstate.define_registered('float_eq', eqer('float'))
pushstate.define_registered('code_eq', eqer('code'))
pushstate.define_registered('boolean_eq', eqer('boolean'))
pushstate.define_registered('string_eq', eqer('string'))

def stackdepther(type):
    '''
    Returns a function that pushes the depth of the appropriate stack of the
    given state.
    '''
    def stackdepth(state):
        return pushstate.push_item(len(state[type]), 'integer', state)
    return stackdepth
pushstate.define_registered('exec_stackdepth', stackdepther('exec'))
pushstate.define_registered('integer_stackdepth', stackdepther('integer'))
pushstate.define_registered('float_stackdepth', stackdepther('float'))
pushstate.define_registered('code_stackdepth', stackdepther('code'))
pushstate.define_registered('boolean_stackdepth', stackdepther('boolean'))
pushstate.define_registered('string_stackdepth', stackdepther('string'))

def yanker(type):
    '''
    Returns a function that yanks an item from deep in the specified stack,
    using the top integer to indicate how deep.
    '''
    def yank(state):
        bool1 = (type == 'integer')
        bool2 = (len(state[type])>1)
        bool3 = (len(state[type])>0)
        bool4 = (len(state['integer'])>0)
        if (bool1 and bool2) or ((not bool1) and bool3 and bool4):
            raw_index = pushstate.stack_ref('integer', 0, state)
            with_index_popped = pushstate.pop_item('integer', state)
            actual_index = max(0, min(raw_index, len(with_index_popped[type]) - 1))
            item = pushstate.stack_ref(type, actual_index, with_index_popped)
            with_item_pulled = with_index_popped[type][:actual_index].append( with_index_popped[type][actual_index+1:])
            state = pushstate.push_item(item, type, with_item_pulled)
        return state
    return yank
pushstate.define_registered('exec_yank', yanker('exec'))
pushstate.define_registered('integer_yank', yanker('integer'))
pushstate.define_registered('float_yank', yanker('float'))
pushstate.define_registered('code_yank', yanker('code'))
pushstate.define_registered('boolean_yank', yanker('boolean'))
pushstate.define_registered('string_yank', yanker('string'))

def yankduper(type):
    '''
    Returns a function that yanks a copy of an item from deep in the specified stack,
    using the top integer to indicate how deep.
    '''
    def yankdup(state):
        bool1 = (type == 'integer')
        bool2 = (len(state[type])>1)
        bool3 = (len(state[type])>0)
        bool4 = (len(state['integer'])>0)
        if (bool1 and bool2) or ((not bool1) and bool3 and bool4):
            raw_index = pushstate.stack_ref('integer', 0, state)
            with_index_popped = pushstate.pop_item('integer', state)
            actual_index = max(0, min(raw_index, len(with_index_popped[type]) - 1))
            item = pushstate.stack_ref(type, actual_index, with_index_popped)
            state = pushstate.push_item(item, type, with_index_popped)
        return state
    return yankdup
pushstate.define_registered('exec_yankdup', yankduper('exec'))
pushstate.define_registered('integer_yankdup', yankduper('integer'))
pushstate.define_registered('float_yankdup', yankduper('float'))
pushstate.define_registered('code_yankdup', yankduper('code'))
pushstate.define_registered('boolean_yankdup', yankduper('boolean'))
pushstate.define_registered('string_yankdup', yankduper('string'))

def shover(type):
    '''
    Returns a function that shoves an item deep in the specified stack, using the top
    integer to indicate how deep.
    '''
    def shove(state):
        bool1 = (type == 'integer')
        bool2 = (len(state[type])>1)
        bool3 = (len(state[type])>0)
        bool4 = (len(state['integer'])>0)
        if (bool1 and bool2) or ((not bool1) and bool3 and bool4):
            raw_index = pushstate.stack_ref('integer', 0, state)
            with_index_popped = pushstate.pop_item('integer', state)
            item = pushstate.top_item(type, with_index_popped)
            with_args_popped = pushstate.pop_item(type, with_index_popped)
            actual_index = max(0, min(raw_index, len(with_args_popped[type])))
            return with_args_popped.insert(actual_index, item)
        else:
            return state
    return shove
pushstate.define_registered('exec_shove', shover('exec'))
pushstate.define_registered('integer_shove', shover('integer'))
pushstate.define_registered('float_shove', shover('float'))
pushstate.define_registered('code_shove', shover('code'))
pushstate.define_registered('boolean_shove', shover('boolean'))
pushstate.define_registered('string_shove', shover('string'))
