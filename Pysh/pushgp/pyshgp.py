'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import globals
from .. import util
from .. import random_push
from .. import individual
from .. import evaluate
import Pysh.globals
import Pysh.util
import Pysh.random_push
import Pysh.individual
import Pysh.evaluate
import Pysh.pushgp.breed
import Pysh.pushgp.genetic_operators
import Pysh.pushgp.parent_selection
import Pysh.pushgp.report

def rand1():
    return random_push.lrand_int(100)

def rand2():
    return random_push.lrand()

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