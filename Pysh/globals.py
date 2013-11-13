'''
Created on Oct 26, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
push_types = ['exec', 'integer', 'float', 'code', 
              'boolean', 'string', 'auxiliary', 'return', 'environment']

max_number_magnitude = 1000000000000 # Used by keep_number_reasonable as the maximum size of any integer or float
min_number_magnitude = 1.0E-10 # Used by keep_number_reasonable as the minimum magnitude of any float
max_string_length = 500 # Used by string instructions to ensure that strings don't get too large
min_random_integer = -10 # The minumum value created by the integer_rand instruction
max_random_integer = 10 # The maximum value created by the integer_rand instruction
min_random_float = -1.0 # The minumum value created by the float_rand instruction
max_random_float = 1.0 # The maximum value created by the float_rand instruction
min_random_string_length = 1 # The minimum length of string created by the string_rand instruction
max_random_string_length = 10 # The maximum length of string created by the string_rand instruction
max_points_in_random_expressions = 50 # The maximum length of code created by the string_rand instruction

timer = 0
timing_map = {'initialization' : 0, 
              'reproduction' : 0, 
              'report' : 0,
              'fitness' : 0,
              'other' : 0}
solution_rates = [0]
elitegroups = []

#The globals below may be reset by arguments to pushgp

### These definitions are used by Push instructions and therefore must be global
#??????? global_atom_generators # The instructions and literals that may be used in Push programs. ??????? 
global_max_points = 100 # The maximum size of a Push program. Also, the maximum size of code that can appear on the exec or code stacks.
global_tag_limit = 10000 # The size of the tag space

### These definitions are used by run-push (and functions it calls), and must be global since run-push is called by the problem-specifc error functions
global_top_level_push_code = True # When true, run-push will push the program's code onto the code stack prior to running
global_top_level_pop_code = True # When true, run-push will pop the code stack after running the program
global_evalpush_limit = 150 # The number of Push instructions that can be evaluated before stopping evaluation
global_evalpush_time_limit = 0 # The time in nanoseconds that a program can evaluate before stopping, 0 means no time limit
global_pop_when_tagging = 0 # When true, tagging instructions will pop the exec stack when tagging; otherwise, the exec stack is not popped

#Special defs not used by Push instructions, but still need to be globally def'ed, go here.
global_use_bushy_code = False