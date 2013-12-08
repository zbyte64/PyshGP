'''
Created on Oct 26, 2013

@author: Eddie
'''

'''
# Testing Interpreter 1 #
#########################
import interpreter
import pushstate

starting_state = pushstate.make_push_state()

starting_code = '(1 (3 2 integer_mult) (5 2 integer_add) integer_mult)'

final_state = interpreter.run_push(starting_code, starting_state, True, True, True, True)
print
print('FINAL:')
print('======')
pushstate.state_pretty_print(final_state)
'''

# Testing Code Generation #
###########################
import random_push
import interpreter
import Pysh.pushstate


#print random_push.decompose(100, 100)

atom_generators = Pysh.pushstate.registered_instructions
atom_generators.append([random_push.lrand_int(100), random_push.lrand()])
#print atom_generators

random_code = random_push.random_code(50, atom_generators)
print random_code
print

starting_state = Pysh.pushstate.make_push_state()
final_state = interpreter.run_push(random_code, starting_state, True, True, True, False)