'''
Created on Dec 6, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
from .. import util
from .. import globals
from .. import pushstate

def code_append(state):
    if len(state['code'])>1:
        new_item = util.ensure_list(pushstate.stack_ref('code', 0, state)) + util.ensure_list(pushstate.stack_ref('code', 1, state))
        if util.count_points(new_item) <= globals.global_max_points:
            return pushstate.push_item(new_item, 'code', pushstate.pop_item('code', pushstate.pop_item('code', state)))
        else:
            return state
    else:
        return state
pushstate.define_registered('code_append', code_append)

def code_atom(state):
    if len(state['code'])>0:
        state = pushstate.push_item(type(pushstate.stack_ref('code', 0, state)) != list, 'boolean', state)
    return state
pushstate.define_registered('code_atom', code_atom)

def code_car(state):
    if len(state['code'])>0 and len(util.ensure_list(pushstate.stack_ref('code', 0, state)))>0:
        state = pushstate.push_item(util.ensure_list(pushstate.stack_ref('code', 0, state))[0], 'code', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_car', code_car)

def code_cdr(state):
    if len(state['code'])>0:
        state = pushstate.push_item(util.ensure_list(pushstate.stack_ref('code', 0, state))[:1], 'code', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_cdr', code_cdr)

def code_cons(state):
    if len(state['code'])>1:
        new_item = [pushstate.stack_ref('code', 1, state)] + util.ensure_list(pushstate.stack_ref('code', 0, state))
        if util.count_points(new_item) <= globals.global_max_points:
            state = pushstate.push_item(new_item, 'code', pushstate.pop_item('code', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_cons', code_cons)
            
def code_do(state):
    if len(state['code'])>0:
        state = pushstate.push_item(pushstate.stack_ref('code', 0, state), 'exec', pushstate.push_item('code_pop', 'exec', state))
    return state
pushstate.define_registered('code_do', code_do)

def code_do_star(state):
    '''
    code_do* in clojush
    '''
    if len(state['code'])>0:
        state = pushstate.push_item(pushstate.stack_ref('code', 0, state), 'exec', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_do*', code_do_star)

def code_do_star_range(state):
    '''
    code_do*range
    '''
    if len(state['code'])>0 and len(state['integer'])>1:
        to_do = state['code'][0]
        current_index = state['integer'][1]
        destination_index = state['integer'][0]
        args_popped = pushstate.pop_item('integer', pushstate.pop_item('integer', pushstate.pop_item('code', state)))
        
        if current_index < destination_index:
            increment = 1
        elif current_index > destination_index:
            increment = -1
        else:
            increment = 0
        
        if increment == 0:
            continuation = args_popped
        else:
            continuation = pushstate.push_item([(current_index+ increment), destination_index, 'code_quote', to_do, 'code_do*range'], 'exec', args_popped)
        
        state = pushstate.push_item(to_do, 'exec', pushstate.push_item(current_index, 'integer', continuation))
    return state
pushstate.define_registered('code_do*range', code_do_star_range)

def exec_do_star_range(state):
    '''
    exec_do*range
    '''
    if len(state['exec'])>0 and len(state['integer'])>1:
        to_do = state['exec'][0]
        current_index = state['integer'][1]
        destination_index = state['integer'][0]
        args_popped = pushstate.pop_item('integer', pushstate.pop_item('integer', pushstate.pop_item('exec', state)))
        
        if current_index < destination_index:
            increment = 1
        elif current_index > destination_index:
            increment = -1
        else:
            increment = 0
        
        if increment == 0:
            continuation = args_popped
        else:
            continuation = pushstate.push_item([(current_index+ increment), destination_index, 'exec_do*range', to_do], 'exec', args_popped)
        
        state = pushstate.push_item(to_do, 'exec', pushstate.push_item(current_index, 'integer', continuation))
    return state
pushstate.define_registered('exec_do*range', exec_do_star_range)

def code_do_star_count(state):
    '''
    code_do*count
    '''
    if len(state['integer'])>0 and state['integer'][0] > 1 and len(state['code'])>0:
        state = pushstate.push_item([0, state['integer'][0]-1, 'code_quote', state['code'][0], 'code_do*range'], 
                                    'exec', 
                                    pushstate.pop_item('integer', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_do*count', code_do_star_count)

def exec_do_star_count(state):
    '''
    exec_do*count
    '''
    if len(state['integer'])>0 and state['integer'][0] > 1 and len(state['exec'])>0:
        state = pushstate.push_item([0, state['integer'][0]-1, 'exec_do*range', ['integer_pop']+util.ensure_list(state['exec'])], 
                                    'exec', 
                                    pushstate.pop_item('integer', pushstate.pop_item('exec', state)))
    return state
pushstate.define_registered('exec_do*count', exec_do_star_count) 

def code_map(state):
    if len(state['code'])>0 and len(state['exec'])>0:
        part1 = []
        for item in util.ensure_list(state['code'][0]):
            part1.append(['code_quote', item, state['exec'][0]])
        part3 = []
        for item in util.ensure_list(state['code'][:1]):
            part3.append('code_cons')
        new_item = part1
        new_item.append('code_wrap')
        new_item = new_item + part3
        state = pushstate.push_item(new_item,
                                    'exec',
                                    pushstate.pop_item('code', pushstate.pop_item('exec', state)))
    return state
pushstate.define_registered('code_map', code_map)

def codemaker(type):
    '''
    Returns a function that pops the stack of the given type and pushes the result on the code stack.
    '''
    def makeCode(state):
        if len(state[type])>0:
            state = pushstate.push_item(state[type][0], 'code', pushstate.pop_item(type, state))
        return state
    return makeCode
pushstate.define_registered('code_fromboolean', codemaker('boolean'))
pushstate.define_registered('code_fromfloat', codemaker('float'))
pushstate.define_registered('code_frominteger', codemaker('integer'))
pushstate.define_registered('code_quote', codemaker('exec'))

def code_if(state):
    if len(state['boolean'])>0 and len(state['code'])>1:
        if state['boolean'][0]:
            state = pushstate.push_item(state['code'][1], 'exec', pushstate.pop_item('boolean', pushstate.pop_item('code', pushstate.pop_item('code', state))))
        else:
            state = pushstate.push_item(state['code'][0], 'exec', pushstate.pop_item('boolean', pushstate.pop_item('code', pushstate.pop_item('code', state))))
    return state
pushstate.define_registered('code_if', code_if)

def exec_if(state):
    if len(state['boolean'])>0 and len(state['exec'])>1:
        if state['boolean'][0]:
            state = pushstate.push_item(state['exec'][1], 'exec', pushstate.pop_item('boolean', pushstate.pop_item('exec', pushstate.pop_item('exec', state))))
        else:
            state = pushstate.push_item(state['exec'][0], 'exec', pushstate.pop_item('boolean', pushstate.pop_item('exec', pushstate.pop_item('exec', state))))
    return state
pushstate.define_registered('exec_if', exec_if)

def exec_when(state):
    if len(state['boolean'])>0 and len(state['exec'])>0:
        if state['boolean'][0]:
            state = pushstate.pop_item('boolean', state)
        else:
            state = pushstate.pop_item('boolean', pushstate.pop_item('exec', state))
    return state
pushstate.define_registered('exec_when', exec_when)

def code_length(state):
    if len(state['code'])>0:
        state = pushstate.push_item(len(util.ensure_list(state['code'][0])), 'integer', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_length', code_length)

def code_list(state):
    if len(state['code'])>1:
        new_item = [state['code'][1], state['code'][0]]
        if util.count_points(new_item) <= globals.global_max_points:
            state = pushstate.push_item(new_item, 'code', pushstate.pop_item('code', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_list', code_list)

def code_wrap(state):
    if len(state['code'])>0:
        new_item = [state['code'][0]]
        if util.count_points(new_item) <= globals.global_max_points:
            state = pushstate.push_item(new_item, 'code', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_wrap', code_wrap)

def code_member(state):
    if len(state['code'])>1:
        state = pushstate.push_item(util.ensure_list(state['code'][0]).count(state['code'][1])>0, 'boolean', pushstate.pop_item('code', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_member', code_member)

def exec_noop(state):
    return state
def code_noop(state):
    return state
pushstate.define_registered('exec_noop', exec_noop)
pushstate.define_registered('code_noop', code_noop)

def code_nth(state):
    if len(state['integer'])>0 and len(state['code'])>0 and len(util.ensure_list(state['code'][0]))>0:
        new_item = util.ensure_list(state['code'][0])[abs(state['integer'][0])%len(util.ensure_list(state['code'][0]))]
        state = pushstate.push_item(new_item, 'code', pushstate.pop_item('integer', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_nth', code_nth)

def code_nthcdr(state):
    if len(state['integer'])>0 and len(state['code'])>0 and len(util.ensure_list(state['code'][0]))>0:
        new_item = util.ensure_list(state['code'][0]).remove(util.ensure_list(state['code'][0])[abs(state['integer'][0])%len(util.ensure_list(state['code'][0]))])
        state = pushstate.push_item(new_item, 'code', pushstate.pop_item('integer', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_nthcdr', code_nthcdr)

def code_null(state):
    if len(state['code'])>0:
        item = state['code'][0]
        state = pushstate.push_item(type(item) == list and len(item)>0, 'boolean', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_null', code_null)

def code_size(state):
    if len(state['code'])>0 and len(state['integer'])>0:
        state = pushstate.push_item(util.count_points(state['code'][0]), 'integer', pushstate.pop_item('code', state))
    return state
pushstate.define_registered('code_size', code_size)
        
#Code_extract and Code_insert coming once Zipper work around is found

def code_subst(state):
    if len(state['code'])>2:
        new_item = util.subst(pushstate.stack_ref('code', 2, state),
                              pushstate.stack_ref('code', 1, state),
                              pushstate.stack_ref('code', 0, state))
        if util.count_points(new_item) <= globals.global_max_points:
            state = pushstate.push_item(new_item, 'code', pushstate.pop_item('code', pushstate.pop_item('code', pushstate.pop_item('code', state))))
    return state
pushstate.define_registered('code_subst', code_subst)

def code_contains(state):
    if len(state['code'])>1:
        state = pushstate.push_item(util.contains_subtree(pushstate.stack_ref('code', 1, state),
                                                          pushstate.stack_ref('code', 0, state)), 
                                    'boolean',
                                    pushstate.pop_item('code', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_contains', code_contains)

def code_container(state):
    if len(state['code'])>1:
        state = pushstate.push_item(util.containing_subtree(pushstate.stack_ref('code', 1, state),
                                                          pushstate.stack_ref('code', 0, state)), 
                                    'code',
                                    pushstate.pop_item('code', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_container', code_container)

def positions(pred, coll):
    '''
    Returns a list containing the positions at which pred
    is true for items in coll.
    '''
    indexes = []
    for i in range(len(coll)):
        if pred == coll[i]:
            indexes.append(i)
    return indexes

def code_position(state):
    if len(state['code'])>1:
        new_item = positions([pushstate.stack_ref('code', 1, state)],
                             util.ensure_list(pushstate.stack_ref('code', 0, state)))[0]
        if new_item == None:
            new_item = -1
        state = pushstate.push_item(new_item, 'integer', pushstate.pop_item('code', pushstate.pop_item('code', state)))
    return state
pushstate.define_registered('code_position', code_position)

def exec_k(state):
    if len(state['exec'])>1:
        state= pushstate.push_item(state['exec'][0], 'exec', pushstate.pop_item('exec', pushstate.pop_item('exec', state)))
    return state
pushstate.define_registered('exec_k', exec_k)

def exec_s(state):
    if len(state['exec'])>2:
        stk = state['exec']
        x = stk[0]
        y = stk[1]
        z = stk[2]
        if util.count_points([y, z])<= globals.global_max_points:
            state= pushstate.push_item(x, 'exec',
                                       pushstate.push_item(z, 'exec',
                                                           pushstate.push_item([y, z], 'exec',
                                                                                pushstate.pop_item('exec',
                                                                                                   pushstate.pop_item('exec',
                                                                                                                      pushstate.pop_item('exec', state))))))
    return state
pushstate.define_registered('exec_s', exec_s)

def exec_y(state):
    if len(state['exec'])>0:
        new_item = ['exec_y', state['exec'][0]]
        if util.count_points(new_item) <= globals.global_max_points:
            state = pushstate.push_item(state['exec'][0], 'exec', pushstate.push_item(new_item, 'exec', pushstate.pop_item('exec', state)))
    return state
pushstate.define_registered('exec_y', exec_y)