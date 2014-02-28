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
        if generation is 0:
            file = open(csv_log_filename+'.csv', 'w')
            file.write('generation,individual,total-error,size\n')
            file.close()
        file = open(csv_log_filename+'.csv', 'a')
        for i in range(len(population)):
            s = str(generation) + str(i) + str(population[i]['total-error']) + str(Pysh.util.count_points(population[i]['program']))+'\n'
            file.write(s)
        file.close()

def jsonize_individual(log_fitness_for_all_cases, json_log_program_strings, generation, individual):
    '''
    Takes an individual and returns it with only the items of interest
    for the json logs.
    '''
    part1_ind = {}
    if log_fitness_for_all_cases:
        part1_ind['errors'] = individual['errors']
    part1_ind['total-error'] = individual['total-error']
    part1_ind['generation'] = generation
    part1_ind['size'] = Pysh.util.count_points(individual['program'])
    
    part2_ind = part1_ind
    if json_log_program_strings:
        part2_ind['program'] = str(individual['program'])
    
    part3_ind = part2_ind
    if individual['hah-error'] != None:
        part3_ind['hah-error'] = individual['hah-error']
    if individual['rms-error'] != None:
        part3_ind['rms-error'] = individual['rms-error']
    return part3_ind

def json_print(population, generation, json_log_filename, log_fitness_for_all_cases, json_log_program_strings):
    json_list = []
    for i in population:
        json_list.append(jsonize_individual(log_fitness_for_all_cases, json_log_program_strings, generation, i))
    for i in json_list:
        if i is 0:
            file = open(json_log_filename+'.json', 'w')
            file.write(str(i))
            file.close()
        else:
            file = open(json_log_filename+'.json', 'a')
            file.write(','+str(i))
            file.close()

###################
# Report Printing #
###################

#def lexicase_report():

#def report_and_check_for_sucess

def initial_report():
    '''
    Prints the initial report of a PushGP run.
    '''
    print 'Registered Instructions: ' + str(Pysh.pushstate.registered_instructions)
    print 'Starting PushGP Run'
    #Could print python version
    #Pysh version
    #Git information (last commit, etc.)
    
def final_report(generation, best, argmap):
    '''
    Prints the final report of a PushGP run if the run is successful.
    '''
    print '\n\nSUCESS at generation '+str(generation)
    print 'Successful Program: ' + str(best['program'])
    print 'Errors: ' + str(best['errors'])
    print 'Total Error: ' + str(best['total-error'])
    print 'History: ' + str(best['history'])
    print 'Size: ' + str(Pysh.util.count_points(best['program'])+'\n\n')
    
    Pysh.simplification.auto_simplify(best, argmap['error-function'], argmap['final-pushgp-simplifications'], True, 500)