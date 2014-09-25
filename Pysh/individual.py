'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''

empty_induvidual = {'genome': [],
              'program': [],
              'errors': [],
              'total-error': [],
              'hah-error': [],
              'rms-error': [],
              'history': [],
              'ancestors': [],
              'parent': []}

def make_induvidual(genome = None, program = None, errors = None, total_error = None, weighted_error = None, history = None, ancestors = None, parent = None):
    i = {'genome': genome,
         'program': program,
         'errors': errors,
         'total-error': total_error,
         'weighted-error': weighted_error,
         'history': history,
         'ancestors': ancestors,
         'parent': parent}
    return i

# No lazy sequences in Python
def printable(thing):
    if thing == None:
        return 'None'
    else:
        return thing
    
def individual_string(i):
    s = 'individual.'
    k = ['program', 'errors', 'total-error', 'hah-error', 'rms-error', 'history', 'ancestors', 'parent']
    for i in range(len(k)):
        s = s + k[i] + ': '
        s = s + i[k[i]] + ', '
    return s