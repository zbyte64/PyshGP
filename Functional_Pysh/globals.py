'''
Created on Oct 26, 2013

@author: Eddie Pantridge Hampshire College 2013
'''
push_types = ['exec', 'integer', 'float', 'code', 
              'boolean', 'string']

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


# Rest of Clojush globals coming later