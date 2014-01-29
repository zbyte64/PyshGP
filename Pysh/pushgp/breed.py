'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import globals
from .. import random_push
from .. import simplification
import parent_selection
import genetic_operators

def breed(agt, location, rand_gen, population, argmap):
    '''
    Replaces the state of the given agent with an individual bred from the given population,
    using the given parameters.
    '''
    '''
    argmap = {"mutation_probability" : keys["mutation_probability"],
            "crossover_probability" : keys["crossover_probability"],
            "simplification_probability" : keys["simplification_probability"],
            "gaussian_mutaion_probability" : keys["gaussian_mutaion_probability"],
            "boolean_gsxover_probability" : keys["boolean_gsxover_probability"],
            "deletion_mutaion_probability" : keys["deletion_mutaion_probability"],
            "parentheses_addition_mutation_probability" : keys["parentheses_addition_mutation_probability"],
            "tagging_mutation_probability" : keys["tagging_mutation_probability"],
            "tag_branch_mutation_probability" : keys["tag_branch_mutation_probability"],
            "ultra_probability" : keys["ultra_probability"],
            #Used by select
            "tournament_size" : keys["tournament_size"],
            "trivial_geography_radius" : keys["trivial_geography_radius"],
            #Used by simplification
            "error_function" : keys["error_function"],
            "reproduction_simplifications" : keys["reproduction_simplifications"],
            "maintain_ancestors" : keys["maintain_ancestors"]}
    '''
    
    n = random_push.lrand(rand_gen)
    parent = parent_selection.select(population, location, argmap)
    if n < argmap["mutation_probability"] :
        new_ind = genetic_operators.mutate(parent, argmap)
    elif n < argmap['mutation_probability'] + argmap['crossover_probability']:
        second_parent = parent_selection.select(population, location, argmap)
        new_ind = genetic_operators.crossover(parent, second_parent, argmap)
    elif n < argmap['mutation_probability'] + argmap['crossover_probability'] + argmap['simplification_probability']:
        new_ind = simplification.auto_simplify(parent, argmap['error_function'], argmap['reproduction_simplifications'], False, 1000, argmap['maintain_ancestors'])
    elif n < argmap['mutation_probability'] + argmap['crossover_probability'] + argmap['simplification_probability'] + argmap['gaussian_mutaion_probability']:
        new_ind = genetic_operators.gaussian_mutate(parent, argmap)
    elif n < argmap['mutation_probability'] + argmap['crossover_probability'] + argmap['simplification_probability'] + argmap['gaussian_mutaion_probability'] + argmap['boolean_gsxover_probability']:
        second_parent = parent_selection.select(population, location, argmap)
        new_ind = genetic_operators.boolean_gsxover(parent, second_parent, argmap)
    elif n < argmap['mutation_probability']+argmap['crossover_probability']+argmap['simplification_probability']+argmap['gaussian_mutaion_probability']+argmap['boolean_gsxover_probability']+argmap['deletion_mutaion_probability']:
        new_ind = genetic_operators.delete_mutate(parent, argmap)
    elif n < argmap['mutation_probability']+argmap['crossover_probability']+argmap['simplification_probability']+argmap['gaussian_mutaion_probability']+argmap['boolean_gsxover_probability']+argmap['deletion_mutaion_probability']+argmap['parentheses_addition_mutation_probability']:
        new_ind = genetic_operators.add_parentheses_mutate(parent, argmap)
    elif n < argmap['mutation_probability']+argmap['crossover_probability']+argmap['simplification_probability']+argmap['gaussian_mutaion_probability']+argmap['boolean_gsxover_probability']+argmap['deletion_mutaion_probability']+argmap['parentheses_addition_mutation_probability']+argmap['tagging_mutation_probability']:
        new_ind = genetic_operators.tagging_mutate(parent, globals.global_tag_limit, argmap)
    elif n < argmap['mutation_probability']+argmap['crossover_probability']+argmap['simplification_probability']+argmap['gaussian_mutaion_probability']+argmap['boolean_gsxover_probability']+argmap['deletion_mutaion_probability']+argmap['parentheses_addition_mutation_probability']+argmap['tagging_mutation_probability']+argmap['tag_branch_mutation_probability']:
        new_ind = genetic_operators.tag_branch_insertion_mutate(parent, globals.global_tag_limit, argmap)
    elif n < argmap['mutation_probability']+argmap['crossover_probability']+argmap['simplification_probability']+argmap['gaussian_mutaion_probability']+argmap['boolean_gsxover_probability']+argmap['deletion_mutaion_probability']+argmap['parentheses_addition_mutation_probability']+argmap['tagging_mutation_probability']+argmap['tag_branch_mutation_probability']+argmap['ultra_probability']:
        second_parent = parent_selection.select(population, location, argmap)
        new_ind = genetic_operators.ultra(parent, second_parent, argmap)
    else:
        new_ind = parent
    new_ind['parent'] = parent
    return new_ind
        