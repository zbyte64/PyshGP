'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College
'''
import globals


def keep_number_reasonable(n):
    '''
    Returns a version of n that obeys limit parameters.
    '''
    if n > globals.max_number_magnitude:
        n = globals.max_number_magnitude
    elif n < -globals.max_number_magnitude:
        n = -globals.max_number_magnitude
    return n