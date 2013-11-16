'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
import pushstate
import globals
import time

literals = ['integer', 'float', 'string', 'boolean']
def recognize_literal(thing):
    '''
    If thing is a literal, return its type -- otherwise return false.
    '''
    if type(thing) == int:
        return 'integer'
    elif type(thing) == float:
        return 'float'
    elif type(thing) == bool:
        return 'boolean'
    else:
        return False

def execute_instruction(instruction, state):
    '''
    Execute a single Push instruction
    '''
    if instruction == None:
        return state
    else:
        literal_type = recognize_literal(instruction)
        if literal_type != False:
            state = pushstate.push_item(instruction, literal_type, state)
        #elif: IF TAG INSTRCUTION
        #elif: TAGGED_MARCO_CODE
        #elif: instruction Table
        else:
            print("Undefined instruction:" + instruction)
            
    return state
        
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
        print
        bool1 = iteration> globals.global_evalpush_limit
        bool2 = len(s['exec']) == 0 and len(s['environment'])==0
        bool3 = time_limit != 0 and time.time() > time_limit
        if  bool1 or bool2 or bool3:
            if s.has_key('termination') == False:
                    s['termination'] = []
            if len(s['exec'])==0 and len(s['environment'])==0:
                s['termination'].append('normal')
            else:
                s['termination'].append('abnormal')
            running = False
            return s
        else:
            if len(s['exec'])==0:
                s = pushstate.end_environment(s)
                if print_steps:
                    print('State after %s steps (last step: %s):')
                    print(str(iteration) + 'end_environment_from_empty_exec')
                    pushstate.state_pretty_print(s)
                if save_state_sequence:
                    saved_state_sequence.append(s)
                iteration += 1
            else:
                exec_top = pushstate.top_item('exec', s)
                s = pushstate.pop_item('exec', s)
                if type(exec_top) == type([]):
                    print("exec_top was a list!")
                    for i in range(len(exec_top)):
                        s['exec'].append(exec_top[len(exec_top)-i-1])
                else:
                    execution_result = execute_instruction(exec_top, s)
                    if trace == False:
                        s =  execution_result
                    if trace == True:
                        if execution_result.has_key('trace') == False:
                            execution_result['trace'] = []
                        execution_result['trace'].insert(0, exec_top)
                        s =  execution_result
                    elif trace == 'changes':
                        if execution_result == s:
                            s = execution_result
                        else:
                            if execution_result.has_key('trace') == False:
                                execution_result['trace'] = []
                            s = execution_result['trace'].insert(0, exec_top)
                    else:
                        print("Error with trace detection!!")
                if print_steps:
                    print('State after %s steps (last step: %s):')
                    if type(exec_top) == type([]):
                        print str(iteration) + "(...)"
                    else:
                        print(str(iteration) + str(exec_top))
                    pushstate.state_pretty_print(s)
                if save_state_sequence:
                    saved_state_sequence.append(s)
                iteration += 1 

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
        return pushstate.pop_item('code', s)
    else:
        return s