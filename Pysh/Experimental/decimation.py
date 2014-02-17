'''
Created on Feb 17, 2014

@author: Eddie Pantridge Hampshire College
'''

import Pysh.random_push

def decimate(population, target_size, tournament_size, radius):
    '''
    Returns the subset of the provided population remaining after sufficiently many
    elimination tournaments to reach the provided target-size.
    '''
    popsize = len(population)
    while popsize > target_size:
        first_location = Pysh.random_push.lrand_int(popsize)
        tournament_index_set = [first_location]
        for i in range(tournament_size-1):
            if radius == 0:
                tournament_index_set.append(Pysh.random_push.lrand_int(popsize))
            else:
                tournament_index_set.append(((Pysh.random_push.lrand_int((radius*2)+1) - radius) + first_location) % popsize)
        victim_index = 0
        for i in range(len(tournament_index_set)):
            if population[i]['total-error'] > population[victim_index]['total-error']:
                victim_index = i
        del population[victim_index]
    return population