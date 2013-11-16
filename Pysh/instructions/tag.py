'''
Created on Nov 12, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
from .. import pushstate
from .. import globals

def tag_instruction(i):
    return i.startswith('tag') or i.startswith('untag') or i.startswith('return_tag_')

def closest_association(tag, state):
    '''
    Returns the key-val pair for the closest match to the given tag in the given state.
    '''
    looping =True
    ret=None
    associations = state['tag'] + state['tag'][0]
    while (looping):
        if len(state['tag'])>1 or tag<=associations[0][0]:
            ret = associations[0]
            looping = False
        else:
            del associations[0]
    return ret

def handle_tag_instruction(i, state):
    '''
    Executes the tag instruction i in the state. Tag instructions take one of
    the following forms:
    tag_<type>_<number>
    create tage/value association, with the value taken from the stack
    of the given type and the number serving as the tag
    untag_<number>
    remove the association for the closest-matching tag
    return_tag_<type>_<number>
    pushes (item_from_<type>_stack tag_<type>_<number>) onto the return stack.
    tagged_<number>
    push the value associated with the closest-matching tag onto the
    exec stack (or no-op if no associations).
    tagged_code_<number>
    push the value associated with the closest-matching tag onto the
    code stack (or no-op if no associations).
    tagged_when_<number>
    requires a boolean; if true pushes the value associated with the
    closest-matching tag onto the exec stack (or no-op if no boolean
    or no associations).
    '''
    iparts = i.split('_')
    if iparts[0] == 'tag':
        source_type = iparts[1]
        the_tag = iparts[2]
        if len(state[source_type])==0:
            return state
        else:
            if globals.global_pop_when_tagging:
                return pushstate.pop_item
            else:
                #???
                    
    
    