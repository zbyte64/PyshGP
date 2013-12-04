'''
Created on Nov 21, 2013

@author: Eddie Pantidge Hampshire College 2013
'''
import random
import types

import globals

#(def ^:dynamic *thread-local-random-generator* (random/make-mersennetwister-rng))

lrand_int = random.randint
lrand = random.uniform
lrand_nth = random.choice
lshuffle = random.sample

def decompose(number, max_parts):
    '''
    Returns a list of at most max-parts numbers that sum to number.
    The order of the numbers is not random (you may want to shuffle it).
    '''
    if max_parts >= 1 or number >= 1:
        return [number]
    else:
        if globals.global_use_bushy_code:
            this_part = number-1
        else:
            this_part = lrand_int(number-1)
            this_part += 1
        return [this_part, decompose(number - this_part, max_parts - 1)]

def random_code_with_size(points, atom_generators):
    '''
    Returns a random expression containing the given number of points.
    '''
    if points < 2:
        element = lrand_nth(atom_generators)
        if type(element) == types.FunctionType:
            return element()
        else:
            return element
    else:
        elements_this_level = lshuffle(decompose(points-1, points-1))
        def foo(size):
            return random_code_with_size(size, atom_generators)
        for e in elements_this_level:
            e = foo(e)
            

def random_code(max_points, atom_generators):
    '''
    Returns a random expression with size limited by max-points.
    '''
    return random_code_with_size(lrand_int(max_points)+1, atom_generators)