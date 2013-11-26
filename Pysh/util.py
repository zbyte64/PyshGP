'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College
'''
import globals
        
def push_to_python(pushCode):
    pyString = []
    for c in pushCode:
        if c == '(':
            pyString.append('[')
        elif c == ')':
            pyString.append(']')
        elif c == ' ':
            pyString.append(', ')
        else:
            pyString.append(c)
    pyString = ''.join(pyString)
    print pyString
    
    #Add ' ' around strings and it should work
    
    pyList = eval(pyString)
    return pyList
    
print push_to_python('(1 (3 2 int_mult) (5 2 int_add) int_mult)')

def keep_number_reasonable(n):
    '''
    Returns a version of n that obeys limit parameters.
    '''
    if n > globals.max_number_magnitude:
        n = globals.max_number_magnitude
    elif n < -globals.max_number_magnitude:
        n = -globals.max_number_magnitude
    return n