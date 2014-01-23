'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''

induvidual = {'program': [],
              'errors': [],
              'total_error': [],
              'hah_error': [],
              'rms_error': [],
              'history': [],
              'ancestors': [],
              'parent': []}

def make_induvidual(program = None, errors = None, total_error = None, hah_error = None, rms_error = None, history = None, ancestors = None, parent = None):
    i = induvidual
    i['program'] = program
    i['errors'] = errors
    i['total_error'] = total_error
    i['hah_error'] = hah_error
    i['rms_error'] = rms_error
    i['history'] = history
    i['ancestors'] = ancestors
    i['parent'] = parent
    return i

# No lazy sequences in Python
def printable(thing):
    if thing == None:
        return 'None'
    else:
        return thing
    
def individual_string(i):
    s = 'individual.'
    k = ['program', 'errors', 'total_error', 'hah_error', 'rms_error', 'history', 'ancestors', 'parent']
    for i in range(len(k)):
        s = s + k[i] + ': '
        s = s + i[k[i]] + ', '
    return s