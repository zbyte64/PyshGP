'''
Created on Apr 22, 2014

@author: Eddie Pantridge
'''

import Pysh.pushgp.pyshgp
import Pysh.random_push
import Pysh.pushstate
import Pysh.interpreter

def inpt(state):
    Pysh.pushstate.push_item(Pysh.pushstate.stack_ref('auxiliary ', 0, state), 'integer', state)
Pysh.pushstate.define_registered('inpt', inpt)

def error_func(program):
    errors = []
    for input in range(0, 10):
        state = Pysh.interpreter.run_push(program,
                                          Pysh.pushstate.push_item(input, 'auxiliary', Pysh.pushstate.push_item(input, 'integer', Pysh.pushstate.make_push_state())))
        top_bool = Pysh.pushstate.top_item('boolean', state)
        if top_bool == "NO-STACK-ITEM":
            errors.append(1000)
        else:
            if top_bool == input % 2:
                errors.append(0)
            else:
                errors.append(1)
    return errors    
            
atom_generators = Pysh.pushstate.registered_nonrandom()

argmap = {'use-single-thread' : True,
          'error-function' : error_func,
          'atom-generators' : atom_generators}

Pysh.pushgp.pyshgp.pushpg(argmap)