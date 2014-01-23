'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import globals
from .. import random_push
from .. import simplification
import parent_selection
import genetic_operators

def breed(agt, location, rand_gen, population, keys):
    '''
    Replaces the state of the given agent with an individual bred from the given population,
    using the given parameters.
    '''
    argmap = {"mutation_probability" : keys["keys"][0],
            "crossover_probability" : keys["keys"][0],
            "simplification_probability" : keys["keys"][0],
            "gaussian_mutaion_probability" : keys["keys"][0],
            "boolean_gsxover_probability" : keys["keys"][0],
            "deletion_mutaion_probability" : keys["keys"][0],
            "parentheses_addition_mutation_probability" : keys["keys"][0],
            "tagging_mutation_probability" : keys["keys"][0],
            "tag_branch_mutation_probability" : keys["keys"][0],
            "ultra_probability" : keys["keys"][0],
            #Used by select
            "tournament_size" : keys["keys"][0],
            "trivial_geography_radius" : keys["keys"][0],
            #Used by simplification
            "error_function" : keys["keys"][0],
            "reproduction_simplifications" : keys["keys"][0],
            "maintain_ancestors" : keys["keys"][0]}
    
    n = random_push.lrand(rand_gen)
    parent = parent_selection.select(population, location, argmap)