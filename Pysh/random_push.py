'''
Created on Nov 21, 2013

@author: Eddie Pantidge Hampshire College 2013
'''
import random
import types

import globals
import util
import translate

#(def ^:dynamic *thread-local-random-generator* (random/make-mersennetwister-rng))

def lrand_int(x):
    return random.randint(1,x)-1

def lrand(x=1):
    return random.uniform(0, x)

def lrand_nth(seq):
    return random.choice(seq)

def lshuffle(population):
    random.shuffle(population)
    return population

################################
# random plush genome generator

def random_closes(close_parens_probabilities):
    '''
    Returns a random number of closes based on close-parens-probabilities, which
    defaults to [0.772 0.206 0.021 0.001]. This is roughly equivalent to each selection
    coming from a binomial distribution with n=4 and p=1/16.
    '''
    prob = lrand()
    parens = 0
    probabilities = util.reductions_add(close_parens_probabilities) + [1.0]
    
    while prob > probabilities[0]:
        parens = parens + 1
        probabilities = probabilities[1:]
    return parens

def random_plush_instruction_map(atom_generators, argmap={'epigenetic-markers' : [],
                                                          'close-parens-probabilities' : [0.772, 0.206, 0.021, 0.001],
                                                          'silent-instruction-probability' : 0}):
        markers = argmap['epigenetic-markers'] + ['instructions']
        ret = {}
        for m in markers:
            if m == 'istructions':
                element = lrand_nth(atom_generators)
                if type(element) == types.FunctionType:
                    fn_element = element()
                    if type(fn_element) == types.FunctionType:
                        ret[m] =  element()
                    else:
                        ret[m] = element
                else:
                    ret[m] = element
            elif m == 'close':
                ret[m] = random_closes(argmap['close-parens-probabilities'])
            elif m == 'silent':
                if lrand() < argmap['silent-instruction-probability']:
                    ret[m] = True
                else:
                    ret[m] = False
        return ret
    
def random_plush_genome_with_size(points, atom_generators, argmap):
    '''
    Returns a random Plush genome containing the given number of points.
    '''
    ret = []
    for i in range(points):
        ret.append(random_plush_instruction_map(atom_generators, argmap))
    return ret

def random_plush_genome(max_points, atom_generators, argmap={}):
    '''
    Returns a random Plush genome with size limited by max-points.
    '''
    return random_plush_genome_with_size(lrand_int(max_points)+1, atom_generators, argmap)
        
#############################
# Random Push Code generators

def random_push_code(max_points, atom_generators, argmap={}):
    '''
    Returns a random Push expression with size limited by max-points.
    '''
    return translate.translate_plush_genome_to_push_program({'genome' : random_plush_genome(max_points, atom_generators, argmap)})

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
        code = []
        for e in elements_this_level:
            code.append(foo(e))
        return code
            

def random_code(max_points, atom_generators):
    '''
    Returns a random expression with size limited by max-points.
    '''
    return random_code_with_size(lrand_int(max_points)+1, atom_generators)

