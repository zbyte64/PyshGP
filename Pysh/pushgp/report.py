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

def sort_by_util(err_fn, population):
    for i in range(len(population)):
        for j in range(len(population)-1):
            if population[j][err_fn] >= population[j+1][err_fn]:
                temp = population[j]
                population[j] = population[j+1]
                population[j+1] = temp
    return population

def report_and_check_for_sucess(population, generation, argmap):
    print
    print ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'
    print ';; Report at generation ' + str(generation)
    
    if argmap['use-rmse']:
        err_fn = 'rms-error'
    else:
        err_fn = 'total-error'
    sorted = sort_by_util(err_fn, population)
    err_fn_best = sorted[1]
    psr_best = argmap['problem-specific-report'](err_fn_best, population, generation, argmap['error-function'], argmap['report-simplifications'])
    if type(psr_best) == list and psr_best.keys() == ['program', 'errors', 'total-error', 'hah-error', 'rms-error', 'history', 'ancestors parent']:
        best = psr_best
    else:
        best = err_fn_best
    
    if argmap['print-error-frequencies-by-case']:
        a = ['']
        for i in population:
            a.append(i['error'])
        print 'Error frequencies by case: ' + str(a)
    if argmap['use-lexicase-selection']:
        print('CANNOT REPORT ON LEXICASE')
    print '--- Best Program based on (error function) Statistics ---'
    print 'Best program: ' + str(best['program'])
    if argmap['report-simplifications'] > 0:
        print 'Partial simplification:'
        print str(Pysh.simplification.auto_simplify(best, argmap['error-function'], argmap['report-simplifications'], False, 1000))
    if argmap['print-errors']:
        print 'Errors: ' + str(best['errors'])
    print 'Total: ' + str(best['total-error'])
    print 'Mean: ' + str(float((best['total-error'])/len(best['errors'])))
    if argmap['use-historically-assessed-hardness']:
        print 'HAH-error: ' + best['hah-error']
    if argmap['use-rmse']:
        print 'RMS-error: ' + str(best['rms-error'])
    if argmap['print-history']:
        print 'History: ' + best['history']
    print 'Size: ' + Pysh.util.count_points(best['program'])
    print 'Percent parens: ' + str(Pysh.util.count_parens(best['program'])/Pysh.util.count_points(best['program']))
    print '--- Population Statistics ---'
    if argmap['print-cosmos-data']:
        print 'WHAT IS COSMOS DATA?'
    popTE = 0;
    for i in population:
        popTE += i['total-error']
    avgTE = popTE/len(population)
    print 'Average total errors in population: ' + str(avgTE)
    medTE = 0
    population[len(population)/2]['total-error']
    if argmap['print-errors']:
        print 'ERROR MINIMA AND AVERAGE SIZE PRINTING COMING SOON'
    totalSize = 0;
    for i in population:
        totalSize += Pysh.util.count_points(i['program'])
    avgSize = totalSize/len(population);
    print 'Average program size in population (points): ' + avgSize
    print'INFO ON UNIQUIE PROGRAMS AND FREQUENCIES COMING SOON'
    print 'INFO ON TIMING COMING SOON'
    if argmap['print-cvs-logs']:
        csv_print(population, generation, argmap['cvs-log-filename'], argmap['log-fitnesses-for-all-cases']);
    if argmap['prin-json-logs']:
        json_print(population, generation, argmap['json-log-filename'], argmap['log-fitness-for-all-cases'], argmap['json-log-program-strings']);
    if (best['total-error'] <= argmap['error-threshold']) or (best['succes']):
        return best
    elif generation >= argmap['max-generations']:
        return 'failure'
    else:
        return 'continue'
    

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