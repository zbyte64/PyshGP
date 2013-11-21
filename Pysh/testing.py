'''
Created on Oct 26, 2013

@author: Eddie
'''
import interpreter
import pushstate

starting_state = pushstate.make_push_state()

#starting_code = [1, 2, 'integer_add']
#starting_code = [1, 2, 3, 4, 5, 'integer_add', 'integer_sub', 'integer_mult', [24, 'integer_div'], 'integer_add']
#starting_code = [True, True, 'boolean_and', False, 'boolean_and', True, 'boolean_or']
starting_code = ['World', 'Hello ', 'string_concat', 'string_length', ['hello_543210', 'string_reverse']]

final_state = interpreter.run_push(starting_code, starting_state, True, True, True)
print
print('FINAL:')
print('======')
pushstate.state_pretty_print(final_state)