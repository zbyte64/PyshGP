'''
Created on Oct 26, 2013

@author: Eddie
'''
import interpreter
import pushstate

starting_state = pushstate.make_push_state()

starting_code = '(1 (3 2 integer_mult) (5 2 integer_add) integer_mult)'

final_state = interpreter.run_push(starting_code, starting_state, True, True, True)
print
print('FINAL:')
print('======')
pushstate.state_pretty_print(final_state)