'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
import math

import util
import pushstate
import random_push
import globals
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
    