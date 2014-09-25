'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
import math

import util
import pushstate
import random_push
import Pysh.globals
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

def normalize_errors(errors, normalization, max_error):
    '''
    Normalizes errors to [0,1] if normalize isn't :none.
    '''
    if normalization is "none":
        return errors
    else:
        for e in errors:
            if normalization is "divide-by-max-error":
                if e >= max_error:
                    e = 1.0
                else:
                    e = e/max_error
            elif normalization is "e-over-e-plus-1":
                e = e/e+1
            else:
                raise Exception("Unrecognized argument for normalization: " + normalization)
        return errors

def evaluate_individual(i, error_function, rand_gen, argmap = {'reuse-errors' : True, 
                                                             'print-history' : False,
                                                             'total-error-method' : 'sum',
                                                             'normalization' : 'none',
                                                             'max-error' : 1000}):
    '''
    Returns the given individual with errors, total-errors, and hah-errors,
    computing them if necessary.
    '''
    p = i['program']
    if i['errors'] !=None and argmap['reuse-errors']:
        e = i['errors']
    else:
        Pysh.globals.evaluations_count += 1
        e = normalize_errors(error_function(p), argmap['normalization'], argmap['max-error'])
    if i['total-error']!=None and argmap['reuse-errors']:
        te = i['total-error']
    else:
        te = compute_total_error(e)
    if argmap['total-error-method'] is 'sum':
        we = None
    elif argmap['total-error-method'] is 'ifs':
        we = None
    elif argmap['total-error-method'] is 'hah':
        we = compute_hah_error(i['errors'])
    elif argmap['total-error-method'] is 'rmse':
        we = compute_root_mean_square_error(i['errors    '])
    
    if argmap['print-history']:
        his = te + i['history']
    else:
        his = i['history']
        
    return individual.make_induvidual(program =p, genome = i['genome'], errors =e, total_error =te, weighted_error =we,
                                      history = his, ancestors = i['ancestors'], parent = i['parent'])