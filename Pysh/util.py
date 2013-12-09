'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College
'''
import globals
        
class Zipper(object):
    def __init__(self, tree, parent = None):
        self.leaves = []
        self.data = None
        self.parent = parent
        
        for e in tree:
            if type(e) == list:
                self.leaves.append(Zipper(e, self))
            else:
                self.leaves.append(e)
    
    def zipper_print(self):
        for e in self.leaves:
            print 'down'
            if type(e) == Zipper:
                e.zipper_print()
            else:
                print e
            print 'up'
            
    def root(self):
        if self.parent != None:
            return self.parent.root()
        else:
            return self

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

<<<<<<< HEAD
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
    
=======
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
            sum +=1
            sum += count_points(e)
        return sum

def code_at_point(tree, point_index):
    '''
    Returns a subtree of tree indexed by point-index in a depth first traversal.
    '''
    index = abs(point_index) % count_points(tree)
    #zipper = 

>>>>>>> 345160a63ece9a8b13aa6e174e4150cd32399162
def keep_number_reasonable(n):
    '''
    Returns a version of n that obeys limit parameters.
    '''
    if n > globals.max_number_magnitude:
        n = globals.max_number_magnitude
    elif n < -globals.max_number_magnitude:
        n = -globals.max_number_magnitude
    return n