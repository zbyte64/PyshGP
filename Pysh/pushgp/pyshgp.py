'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
import Pysh.globals
import Pysh.util
import Pysh.random_push
import Pysh.individual
import Pysh.evaluate
import Pysh.pushgp.breed
import Pysh.pushgp.genetic_operators
import Pysh.pushgp.parent_selection
import Pysh.pushgp.report
import Pysh.Experimental.decimation

import datetime
import random
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def rand1():
    return Pysh.random_push.lrand_int(100)

def rand2():
    return Pysh.random_push.lrand()

push_argmap = {#CLOJUSH SYSTEM ARGUMENTS
            'use-single-thread' : False, #When true, Pysh will only use a single thread
            'random-seed' : 'WHAT IS THIS?', #The seed for the random number generator
            'initial-population' : None, #(MAY BE BROKEN) Can point to a file where an initial population is stored and can be read
            'save-initial-population' : False, #When true, saves the initial population
            #STANDARD GP ARGUMENTS
            'error-function' : 'FUNCTION IN DICTIONARY?', #Function that takes a program and returns a list of errors
            'error-threshold' : 0, #
            'atom-generators' : [Pysh.pushstate.registered_instructions, rand1, rand2],
            'population-size' : 1000,
            'max-generations' : 1001,
            'max-points' : 50,
            'max-points-in-initial-program' : 50,
            'evalpush-limit' : 150,
            'evalpush-time-limit' : 0,
            'reuse-errors' : True,
            #GENETIC OPERATOR PROBABILITIES (replication-probability is 1.0 minus the rest)
            'reproduction-probability' : 0.1,
            'mutation-probability' : 0.4,
            'crossover-probability' : 0.5,
            'simplification-probability' : 0.0,
            'ultra-probability' : 0.0,
            'gaussian-mutation-probability' : 0.0,
            'boolean-gsxover-probability' : 0.0,
            'deletion-mutation-probability' : 0.0,
            'parentheses-addition-mutaion-probability' : 0.0,
            'tagging-mutaion-probability' : 0.0,
            'tag-branch-mutation-probability' : 0.0,
            #ARGUMENTS RELATED TO GENETIC OPERATORS,
            'mutation-max-points' : 20, # The maximum number of points that new code will introduce during mutation
            'reproduction-simplifications' : 1, # The number of simplification steps that will happen during simplification reproduction
            'ultra-alternation-rate' : 0.1, # When using ULTRA, how often ULTRA alternates between the parents
            'ultra-alignment-deviation' : 1, # When using ULTRA, the standard deviation of how far alternation may jump between indices when switching between parents
            'ultra-mutation-rate' : 0.1, # The probability of each token being mutated during ULTRA
            'use-ultra-no-paren-mutation' : False, # If True, ULTRA will use no-paren mutation, which means that parentheses won't be added or deleted during mutation.
            'ultra-pads-with-empties' : False, # If True then ULTRA pads the smaller parent with () and then removes them# if False then this is instead done using the symbol 'ultra-padding.
            'gaussian-mutation-per-number-mutation-probability' : 0.5, # The probability that any given float literal will be affected by a pass of gaussian-mutate
            'gaussian-mutation-standard-deviation' : 0.1, # The standard deviation of a gaussian-mutated float
            'boolean-gsxover-new-code-max-points' : 20, # The maximum size of the random code fragment used in boolean-gsxover
            'tag-branch-mutation-type-instruction-pairs' : [], # A list of types and comparators that can be used by tag-branch-insertion-mutation
            #ARGUMENTS RELATED TO NODE SELECTION (used in mutate, crossover, and tagging-mutate)
            'node-selection-method' : 'unbiased', # The node selection method can be 'unbiased, 'leaf-probability, or 'size-tournament
            'node-selection-leaf-probability' : 0.1, # If the node-selection-method is 'leaf-probability, this is the percent of selections that will happen in leaves of the tree
            'node-selection-tournament-size' : 2, # If node-selection-method is 'size-tournament, this is the size of the node selection tournaments
            #ARGUMENTS RELATED TO PARENT SELECTION
            'tournament-size' : 7, # If using tournament selection, the size of the tournaments
            'trivial-geography-radius' : 0, # If non-zero, this is used as the radius from which to select individuals for tournament or lexicase selection
            'decimation-ratio' : 1, # If >= 1, does nothing. Otherwise, is the percent of the population size that is retained before breeding. If 0 < decimation-ratio < 1, decimation tournaments will be used to reduce the population to size (* population-size decimation-ratio) before breeding.
            'decimation-tournament-size' : 2, # Size of the decimation tournaments
            'use-historically-assessed-hardness' : False, # When True, total error for tournament selection will depend on historically-assessed hardness
            'use-rmse' : False, # When True, total error for tournament selection will depend on the root mean square error of the error vector
            'use-lexicase-selection' : False, # If True, uses Lexicase Parent Selection (see Spector paper in GECCO-UP 2012 workshop proceedings)
            'use-elitegroup-lexicase-selection' : False, # If True, uses elitegroup lexicase selection, an experimental change to lexicase that thus far is often worse
            #ARGUMENTS RELATED TO THE PUSH INTERPRETER
            'pop-when-tagging' : True, # When True, tagging instructions will pop the exec stack when tagging# otherwise, the exec stack is not popped
            'tag-limit' : 10000, # The size of the tag space
            'top-level-push-code' : True, # When True, run-push will push the program's code onto the code stack prior to running
            'top-level-pop-code' : True, # When True, run-push will pop the code stack after running the program
            #ARGUMENTS RELATED TO GENERATIONAL AND FINAL REPORTS
            'pushgp-simplifications' : 100, # The number of simplification steps that will happen during pushgp simplifications
            'final-pushgp-simplifications' : 1000, # The number of simplification steps that will happen during final pushgp simplifications
            'problem-specific-pushgp' : 'default-problem-specific-pushgp', # A function can be called to provide a problem-specific pushgp, which happens after the normal generational pushgp is printed
            'print-errors' : True, # When True, prints the error vector of the best individual
            'print-history' : False, # When True, prints the history of the best individual's ancestors' total errors
            'print-timings' : False, # If True, pushgp prints how long different parts of evolution have taken during the current run.
            'print-cosmos-data' : False, # If True, pushgp prints COSMOS data each generation.
            'maintain-ancestors' : False, # If True, save all ancestors in each individual (costly)
            'print-ancestors-of-solution' : False, # If True, final pushgp prints the ancestors of the solution. Requires 'maintain-ancestors to be True.
            #ARGUMENTS RELATED TO PRINTING JSON OR CSV LOGS
            'print-csv-logs' : False, # Prints a CSV log of the population each generation
            'print-json-logs' : False, # Prints a JSON log of the population each generation
            'csv-log-filename' : "log.csv", # The file to print CSV log to
            'json-log-filename' : "log.json", # The file to print JSON log to
            'log-fitnesses-for-all-cases' : False, # If True, the CSV and JSON logs will include the fitnesses of each individual on every test case
            'json-log-program-strings' : False, # If True, JSON logs will include program strings for each individual
            #OTHER ARGUMENTS
            'parent-reversion-probability' : 0.0, # The probability of a child being reverted to its parent if the parent has better fitness or equal fitness and is smaller
            'use-bushy-code' : False, # When True, random code and code changed by ULTRA mutation, will be "bushy", as in close to a binary tree
            }

def load_push_argmap(args):
    for k in push_argmap.keys():
        for k2 in args.keys():
            if k is k2:
                push_argmap[k] = args[k]
        
def reset_globals():
    #AS PUSH ADDS MORE GLOBALS, THIS FUNCTION WILL NEED TO BE UPDATED
    for k, v in push_argmap.iteritems():
        if k is 'atom-generators':
            Pysh.globals.global_atom_generators = push_argmap[k]
        elif k is 'max-points':
            Pysh.globals.global_max_points = push_argmap[k]
        elif k is 'tag-limit':
            Pysh.globals.global_tag_limit = push_argmap[k]
        elif k is 'top-level-push-code':
            Pysh.globals.global_top_level_push_code = push_argmap[k]
        elif k is 'top-level-pop-code':
            Pysh.globals.global_top_level_pop_code = push_argmap[k]
        elif k is 'evalpush-limit':
            Pysh.globals.global_evalpush_limit = push_argmap[k]
        elif k is 'evalpush-time-limit':
            Pysh.globals.global_evalpush_time_limit = push_argmap[k]
        elif k is 'pop-when-tagging':
            Pysh.globals.global_pop_when_tagging = push_argmap[k]
        elif k is 'use-bushy-code':
            Pysh.globals.global_use_bushy_code = push_argmap[k]
            
def make_agents_and_rng(argmap):
    #agent_error_handler
    #random_seeds = []
    if argmap['initial-population']:
        #READ POPULATION IN FROM FILE
        print("NO READING FROM FILE YET")
    else:
        pa = []
        for i in range(argmap['population_size']):
            pa.append(Pysh.individual.make_induvidual(Pysh.random_push.random_code(argmap['max-points-in-initial-program'], argmap['atom-generators'])))
        f = str('data/'+str(datetime.datetime.now())+'.ser')
        if argmap['save-initial-population']:
            print('SORRY NO SAVING POPULATIONS YET')
        
        ca = []
        for i in range(argmap['population_size']):
            ca.append(Pysh.individual.make_induvidual())
        
        rs = []
        for i in range(argmap['population_size']):
            rs.append(random.randint(0, 9999999))
            
        rg = []
        for i in range(argmap['population_size']):
            temp = random.Random()
            temp.seed(rs[i])
            ca.append(temp)
    
    return {'pop-agents':pa, 'child-agents':ca, 'random-seeds':rs, 'rand-gens':rg}
        
def compute_errors(pop_agents, rand_gens, argmap):
    errors = []
    for i in range(len(pop_agents)):
        errors.append(Pysh.evaluate.evaluate_individual(pop_agents[i], argmap['error_function'], rand_gens[i], argmap))
    return errors

def parental_reversion(pop_agents, generation, argmap):
    if generation > 0 and argmap['parent-reversion-probability'] > 0:
        if argmap['use-historically-assessed-hardness']:
            err_fn = "hah-error"
        elif argmap['use-rmse']:
            err_fn = ":rms-error"
        else:
            err_fn = 'total-error'
        print "Performing parent reversion..."
        for i in pop_agents:
            if (i[err_fn] < i['parent'][err_fn]) or ((i[err_fn] == i['parent'][err_fn]) and (Pysh.util.count_points(i['program'])>Pysh.util.count_points(i['parent']['program']))) or (Pysh.random_push.lrand()>argmap['parent-reversion-probability']):
                i['parent'] = None
                return i
            else:
                return i['parent']
        print "Done performing parent reversion."
        
def remove_parents(pop_agents, argmap):
    """
    Removes value from :parent for each individual in the population. This will
    save memory.
    """
    for i in pop_agents:
        i['parent'] = 0
        
### calculate-hah-solution-rates-wrapper ### Still needed?? ###

def produce_new_offspring(pop_agents, child_agents, rand_gens, argmap):
    if argmap["decimal-ratio"]>=1:
        pop = pop_agents
    else:
        pop = Pysh.Experimental.decimation.decimate(pop_agents, int(argmap['decimation-ratio']*argmap['population-size']), argmap['decimation-tournament-size'], argmap['trivial-geography-radius'])
    for i in range(argmap['population-size']):
        child_agents[i] = Pysh.pushgp.breed.breed(child_agents[i], i, rand_gens[i], pop, push_argmap)
        
def install_next_generation(pop_agents, child_agents, argmap):
    for i in range(argmap['population-size']):
        pop_agents[i] = pop_agents[i]['child-agents'][i]
        
def check_genetic_operator_probabilities_add_to_one(argmap):
    prob_keywords = ['mutation-probability', 'crossover-probability', 'simplification-probability', 'ultra-probability', 'guassian-mutaion-probability', 'boolean-gsxover-probability',
                     'deletion-mutaion-probability', 'parentheses-addition-mutation-probability', 'tagging-mutation-probability', 'tag-branch-mutation-probability']
    prob_map = {}
    for key in prob_keywords():
        prob_map[key] = argmap[key]
    prob_total = 0
    for e in prob_map:
        prob_total += e
    if prob_total is 1:
        return True
    else:
        print 'Error probabilities do not add up to 1'
        print 'They add up to: ' + str(prob_total)
        return False

def timer(argmap, step):
    '''
    Used to track the time used by different parts of evolution.
    '''
    if argmap['print-timings']:
        start_time = Pysh.globals.timer
        current_time_for_step = Pysh.globals.timing_map[step]
        Pysh.globals.timer = current_milli_time()
        Pysh.globals.timing_map[step] = current_time_for_step + (Pysh.globals.timer - start_time) 

def pushpg(args = []):
    '''
    The top-level routine of pushgp.
    '''
    Pysh.globals.timer = current_milli_time()
    load_push_argmap(args)
    # set globals from parameters
    reset_globals()
    