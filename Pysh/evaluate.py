'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
import math

import util
import pushstate
import random_push
import globals
import individual

def compute_total_error(errors):
    i = 0
    for e in errors:
        i += e
    return i

def compute_root_mean_square_error(errors):
    i = 0
    for e in errors:
        i += e*e
    i = i/len(errors)
    return math.sqrt(i)

def compute_hah_error(errors):
    def foo(rate, e):
        return (1.01 - rate)*e
    ret = 0
    for i in range(min(len(globals.solution_rates), len(errors))):
        ret += foo(globals.solution_rates[i])
        ret += foo(errors[i])
    return ret

def calculate_hah_solution_rates(use_historically_assessed_hardness, pop_agents, error_threshold, population_size):
    if use_historically_assessed_hardness:
        error_seqs = []
        for i in pop_agents:
            error_seqs.append(i['errors'])
        num_cases = len(error_seqs)
        new_solution_rates = []
        for i in range(num_cases):
            num_below_threshold = 0
            for e in error_seqs:
                if e <= error_threshold:
                    num_below_threshold += 1
            new_solution_rates.append(num_below_threshold/population_size)
        globals.solution_rates = new_solution_rates
    print('\nSolution rates:')
    print(globals.solution_rates)

def evaluate_individual(i, error_function, rand_gen, keys = {'reuse_errors' : True, 
                                                             'print_history' : False,
                                                             'use_rmse' : False,
                                                             'use_historically_assesed_hardness' : False}):
    '''
    Returns the given individual with errors, total-errors, and hah-errors,
    computing them if necessary.
    '''
    p = i['program']
    if len(i['errors'])!=None and keys['reuse_errors']:
        e = i['errors']
    else:
        e = error_function(p)
    if i['total_error']!=None and keys['reuse_errors']:
        te = i['total_error']
    else:
        te = compute_total_error(e)
    if keys['use_historically_assesed_hardness']:
        he = compute_hah_error(e)
    else:
        he = None
    if keys['use_rmse']:
        rmse = compute_root_mean_square_error(e)
    else:
        rmse = None
    if keys['print_history']:
        his = te + i['history']
    else:
        his = i['history']
        
    return individual.make_induvidual(program =p, errors =e, total_error =te, hah_error =he, rms_error =rmse,
                                      history = his, ancestors = i['ancestors'], parent = i['parent'])