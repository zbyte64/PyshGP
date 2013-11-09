'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
import pushstate
import globals
import time

def execute_instruction(instruction, state):
    '''
    Execute a single Push instruction
    '''
    if instruction == None:
        return state
    else:
        #NOT DONE YET
        pass
        
        
saved_state_sequence = []

def eval_push(state, print_steps = False, trace = False, save_state_sequence = False):
    '''
    Executes the contents of the exec stack, aborting prematurely if execution limits are exceeded.
    '''
    iteration = 1
    s = state
    if globals.global_evalpush_time_limit == 0:
        time_limit = 0
    else:
        time_limit = globals.global_evalpush_time_limit + time.time()
    running = True
    while running:
        if  iteration > globals.global_evalpush_limit or (len(s['exec'])>0 and len(s['enviroment'])>0) or (time_limit != 0 and time.time() > time.time()):
            if len(s['exec'])>0 and len(s['enviroment'])>0:
                s['termination'] = 'normal'
            else:
                s['termination'] = 'abnormal'
        else:
            if len(s['exec'])==0:
                #WRITE END_ENVIRONMENT IN PUSHSTATE!
                pass

def run_push(code, state, print_steps = False, trace = False, save_state_sequence = False):
    '''
    The top level of the push interpreter;
    calls eval-push between appropriate code/exec pushing/popping.
    '''
    if globals.global_top_level_push_code:
        s = pushstate.push_item(code, 'code', state)
    s = pushstate.push_item(code, 'exec', state)
    if print_steps:
        print '\nState after 0 steps:'
        pushstate.state_pretty_print(s)
    if save_state_sequence:
        saved_state_sequence = [s]
    s = eval_push(s, print_steps, trace, save_state_sequence)
    if globals.global_top_level_pop_code:
        pushstate.pop_item('code', s)