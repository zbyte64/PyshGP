'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshrie College
'''
import Pysh.util
import Pysh.globals
import Pysh.pushstate
import Pysh.simplification
import Pysh.individual

def default_problem_specific_report(best, population, generation, error_function, report_simplifications):
    '''
    Customize this for your own problem. It will be called at the end of the generational report.
    '''
    return 'no-problem-specific-report-function-defined'

#def git_last_commit_has():

def print_params(push_argmap):
    for k, v in push_argmap.iteritems():
        print str(k) + '=' + str(v)

#####################################################
#   Log Printing

def csv_print(population, generation, csv_log_filename, log_fitness_for_all_cases):
    '''
    Prints a csv of the population, with each individual's fitness and size.
    If log-fitnesses-for-all-cases is true, it also prints the value
    of each fitness case.
    '''
    if not log_fitness_for_all_cases:
        