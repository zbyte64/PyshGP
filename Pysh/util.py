'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College
'''
import globals

def push_to_python(pushCode):
    '''
    takes push code and makes it more python-like for the Pysh interpreter
    '''
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

def python_to_push(pythonCode):
    pythonCode = ''.join(pythonCode)
    print pythonCode
    print
    pushString = []
    for c in pythonCode:
        if c == '[':
            pushString.append('(')
        elif c == ']':
            pushString.append(')')
        elif c == '\'':
            pass
        else:
            pushString.append(c)
    
    pushString = ''.join(pushString)
    return pushString

python_to_push([[1, 2, 5, 100, 'integer_sub'], 'integer_add', 'integer_mult'])
    
def ensure_list(thing):
    if type(thing) == list:
        return thing
    else:
        return [thing]
  
def count_points(tree):
    '''
    Returns the number of points in tree, where each atom and each pair of parentheses counts as a point.
    '''
    if type(tree) == list:
        sum = 0
        for e in tree:
            sum += count_points(e)
        return sum
    else:
        return 1

'''def code_at_point(tree, point_index):
    
    #Returns a subtree of tree indexed by point-index in a depth first traversal.
    
    index = abs(point_index) % count_points(tree)
'''    #zipper = 

def subst(this, that, the_list):
    '''
    Returns the given list but with all instances of that (at any depth)
    replaced with this. Read as 'subst this for that in list'. 
    '''
    ret = []
    for e in the_list:
        if e == that:
            ret.append(this)
        elif type(e) is list:
            ret.append(subst(this, that, e))
        else:
            ret.append(e)
    return ret

def contains_subtree(tree, subtree):
    '''
    Returns true if tree contains subtree at any level.
    '''
    if type(tree) != list:
        return None
    elif len(tree) == 0:
        return None
    elif subtree in tree:
        return tree
    else:
        ret = []
        for e in tree:
            ret.append(contains_subtree(e, subtree))
        ret = filter(lambda x: x is not None, ret)
        return len(ret)>0
    
def containing_subtree(tree, subtree):
    '''
    If tree contains subtree at any level then this returns the smallest
    subtree of tree that contains but is not equal to the first instance of
    subtree. For example, (contining-subtree '(b (c (a)) (d (a))) '(a)) => (c (a)).
    Returns nil if tree does not contain subtree.
    '''
    if type(tree) != list:
        return None
    elif len(tree) == 0:
        return None
    elif subtree in tree:
        return tree
    else:
        ret = []
        for e in tree:
            ret.append(contains_subtree(e, subtree))
        ret = filter(lambda x: x is not None, ret)
        return ret[0]
    
def keep_number_reasonable(n):
    '''
    Returns a version of n that obeys limit parameters.
    '''
    if n > globals.max_number_magnitude:
        n = globals.max_number_magnitude
    elif n < -globals.max_number_magnitude:
        n = -globals.max_number_magnitude
    return n