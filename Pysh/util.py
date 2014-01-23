'''
Created on Oct 30, 2013

@author: Eddie Pantridge Hampshire College
'''
import globals
import collections
import pysh_tree

def push_to_python(pushCode):
    '''
    takes push code and makes it more python-like for the Pysh interpreter
    '''
    inString = False
    pyString = []
    for c in pushCode:
        if c == '\"':
            inString = not inString
            pyString.append('\"')
        elif c == '(':
            pyString.append('[')
        elif c == ')':
            pyString.append(']')
        elif c == ' ' and not inString:
            pyString.append(', ')
        else:
            pyString.append(c)
    pyString = ''.join(pyString)

    errors = True
    progressIndex = 0
    while errors:
        try: pyCode = eval(pyString)
        except NameError as detail:
            s = str(detail)
            start = s.index('\'')+1
            end = s.index('\'', start+1)
            s = s[start:end]
            if s == 'true':
                i = pyString.index(s)
                pyString = pyString[:i] + 'True' + pyString[i+4:]
            elif s == 'false':
                i = pyString.index(s)
                pyString = pyString[:i] + 'False' + pyString[i+5:]
            else:
                orgIndex = pyString.index(s, progressIndex)
                progressIndex = orgIndex
                pyString = pyString[:orgIndex] + pyString[orgIndex+len(s):]
                s = '\'' + s + '\''
                pyString = pyString[:orgIndex] + s + pyString[orgIndex:]
                start += len(s)
        else:
            errors = False      
    return pyCode
#print(push_to_python('(1 2 true integer_add)'))


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

def code_at_point(tree, point_index):
    '''
    Returns a subtree of tree indexed by point-index in a depth first traversal.
    '''
    t = pysh_tree.PyshTreeNode()
    t.loadFromList(tree)
    cn = t
    for i in range(point_index):
        if len(cn.children)>0:
            cn = cn.traverse('down', 0)
        elif len(cn.parent.children)>cn.parent.children.index(cn)+1:
            cn = cn.traverse('right')
        else:
            while len(cn.parent.children)==cn.parent.children.index(cn)+1 and cn.parent != None:
                cn = cn.traverse('up')
            cn = cn.traverse('right')
    return cn.toList()

def insert_code_at_point(tree, point_index, new_subtree):
    '''
    Returns a copy of tree with the subtree formerly indexed by
    point-index (in a depth-first traversal) replaced by new-subtree.
    '''
    t = pysh_tree.PyshTreeNode()
    t.loadFromList(tree)
    cn = t
    for i in range(point_index):
        if len(cn.children)>0:
            cn = cn.traverse('down', 0)
        elif len(cn.parent.children)>cn.parent.children.index(cn)+1:
            cn = cn.traverse('right')
        else:
            while len(cn.parent.children)==cn.parent.children.index(cn)+1 and cn.parent != None:
                cn = cn.traverse('up')
            cn = cn.traverse('right')
    temp = cn.parent
    temp.children[temp.children.index(cn)] = new_subtree
    while temp.parent != None:
        temp = temp.traverse('up')
    if len(temp.toList()) > 0:
        return temp.toList()
    else:
        return tree        
    
def remove_code_at_point(tree, point_index):
    '''
    Returns a copy of tree with the subtree formerly indexed by
    point-index (in a depth-first traversal) removed. If removal would
    result in an empty list then it is not performed. (NOTE: this is different
    from the behavior in other implementations of Push.)
    '''
    t = pysh_tree.PyshTreeNode()
    t.loadFromList(tree)
    cn = t
    for i in range(point_index):
        if len(cn.children)>0:
            cn = cn.traverse('down', 0)
        elif len(cn.parent.children)>cn.parent.children.index(cn)+1:
            cn = cn.traverse('right')
        else:
            while len(cn.parent.children)==cn.parent.children.index(cn)+1 and cn.parent != None:
                cn = cn.traverse('up')
            cn = cn.traverse('right')
    temp = cn.parent
    temp.children.remove(cn)
    while temp.parent != None:
        temp = temp.traverse('up')
    if len(temp.toList()) > 0:
        return temp.toList()
    else:
        return tree
    
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

def all_items(lst):
    '''
    Returns a list of all of the items in lst, where sublists and atoms all
    count as items. Will contain duplicates if there are duplicates in lst.
    '''
    ret = []
    for e in lst:
        if type(e) == list:
            ret += all_items(e)
        else:
            ret.append(e)
    return ret

def walklist(inner, outer, form):
    '''
    Like walk, but only for lists.
    '''
    if type(form) == list:
        newList = []
        for e in form:
            newList.append(inner(e))
        return outer(newList)
    else:
        return outer(form)

#def postwalklist(f, form):
    '''
    Like postwalk, but only for lists.
    REPLACED BY pysh_tree
    '''
            
    
