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

    errors = True
    progressIndex = 0
    while errors:
        try: pyString = eval(pyString)
        except NameError as detail:
            s = str(detail)
            start = s.index('\'')+1
            end = s.index('\'', start+1)
            s = s[start:end]
            orgIndex = pyString.index(s, progressIndex)
            progressIndex = orgIndex
            pyString = pyString[:orgIndex] + pyString[orgIndex+len(s):]
            s = '\'' + s + '\''
            pyString = pyString[:orgIndex] + s + pyString[orgIndex:]
            start += len(s)
        else:
            errors = False
    #print pyString       
    return pyString
    
def keep_number_reasonable(n):
    '''
    Returns a version of n that obeys limit parameters.
    '''
    if n > globals.max_number_magnitude:
        n = globals.max_number_magnitude
    elif n < -globals.max_number_magnitude:
        n = -globals.max_number_magnitude
    return n