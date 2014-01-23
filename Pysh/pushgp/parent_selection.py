'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
from .. import random_push
from .. import globals

def compete(i1, i2, err_fn):
    if (i1[err_fn]<(i2[err_fn])):
        return i1
    else:
        return i2
    
def tournament_selection(pop, location, keys):
    '''
    Returns an individual that does the best out of a tournament.
    '''
    tournament_set = []
    for i in range(keys['tournament-size']):
        if keys['trivial-geography-radius'] == 0:
            nth = random_push.lrand_int(len(pop))
        else:
            nth = (location + (random_push.lrand_int(1+(keys['trivial-geography-radius']*2))-keys['trivial-geography-radius']))
            nth = nth % len(pop)
        tournament_set.append(pop[nth])
    
    if keys['use-historically-assessed-hardness']:
        err_fn = 'hah-error'
    elif keys['use-rmse']:
        err_fn = 'rms-error'
    else:
        err_fn = 'total-error'
    
    winner = tournament_set[0]
    for i in range(len(tournament_set)-1):
        winner = compete(winner, tournament_set[i+1], err_fn)
    return winner

####################################################################
#Lexicase Selection (COMING SOON)
####################################################################
def retain_one_induvidual_per_error_vector(pop):
    '''
    Retains one random individual to represent each error vector.
    '''
    pass

####################################################################
#Parent Selection
####################################################################
def select(pop, location, keys):
    argmap = {'use_lexicase_selection' : keys[0],
              'use_elitegroup_lexicase_selection' : keys[1]}
    if argmap('use_lexicase_selection'):
        pass
        #return lexicase_selection(pop, location, argmap)
    elif argmap('use_elitegroup_lexicase_selection'):
        #return elitegroup_lexicase_selection(pop)
        pass
    else:
        return tournament_selection(pop, location, argmap)
        
    