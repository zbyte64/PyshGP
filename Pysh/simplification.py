'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
import util
import globals
import pushstate
import random_push
import individual
import evaluate

def flatten_seqs(x):
    '''
    A version of flatten that only flattens nested seqs.
    '''
    ret = []
    for e in x:
        if type(e) == list:
            ret += flatten_seqs(e)
        else:
            ret.append(e)
    return ret

def auto_simplify(ind, error_function, steps, printBool, progress_interval, maintain_ancestors = False):
    '''
    Auto-simplifies the provided individual.
    '''
    if printBool:
        print '\nAuto-simplifying with starting size: ' + str(util.count_points(ind['program']))
    looping = True
    step = 0
    program = ind['program']
    errors = ind['errors']
    total_errors = ind['total-error']
    while looping:
        if printBool and (step >= steps or step % progress_interval == 0):
            print '\nstep: ' + step + '\nprogram: ' + str(program) + '\nerrors: ' + str(errors) + '\ntotal: ' + str(total_errors) + '\nsize: ' + str(util.count_points(program))
        if step >= steps:
            if maintain_ancestors:
                ancestors = [ind['program']] + ind['ancestors']
            else:
                ancestors = ind['ancestors']
            return individual.make_induvidual(program = program, errors = errors, total_errors = total_errors, ind['history'], ancestors = ancestors)
        else:
            if random_push.lrand_int(5)< 4:
                p = program
                how_many = random_push.lrand_int(2)+1
                looping2 = True
                while looping2:
                    if how_many == 0:
                        new_program = p
                        looping2 = False
                    else:
                        p = util.remove_code_at_point(p, random_push.lrand_int(util.count_points(p)))
                        how_many -= 1
            point_index = random_push.lrand_int(util.count_points(program))
            point = util.code_at_point(program, point_index)
            if type(point) == list:
                new_program = util.insert_code_at_point(program, point_index, flatten_seqs(point))
            else:
                new_program = program
            new_errors = error_function(new_program)
            new_total_errors = evaluate.compute_total_error(new_errors)
            if new_errors == errors:
                step += 1
                program = new_program
                errors = new_errors
                total_errors = new_total_errors
            else:
                step += 1
                
def auto_simplify_from_program(p, error_function, steps, printBool, progress_interval):
    errs = error_function(p)
    terrs = 0
    for e in errs:
        terrs += e
    return auto_simplify(individual.make_induvidual(program = p, errors = errs, total_error = terrs),
                         error_function, steps, printBool, progress_interval)
                
                
                
                
                
                
                
                
                
                
                
                
        