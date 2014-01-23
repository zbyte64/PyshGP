'''
Created on Dec 21, 2013

@author: Eddie Pantridge Hampshire College
'''
import math

import Pysh.util
import Pysh.random_push
import Pysh.globals
import Pysh.individual
import Pysh.node_selection
import Pysh.pysh_tree

#using ULTRA (Uniform Linear Transformation with Repair and Alternation) operator
def gaussian_noise_factor():
    '''
    Returns gaussian noise of mean 0, std dev 1.
    '''
    i1 = math.sqrt(math.log(Pysh.random_push.lrand()) * -2.0)
    i2 = math.cos(math.pi * Pysh.random_push.lrand() * -2.0)
    return i1 * i2

##### ULTRA #####
def remove_empties(t):
    '''
    Removes empty sequences from tree t.
    '''
    tree = Pysh.pysh_tree.PyshTreeNode()
    tree.loadFromList(t)
    tree.remove_empty_elements()
    return tree.toList()

def remove_ultra_padding(t):
    '''
    Removes instances of 'ultra-padding from tree t.
    '''
    tree = Pysh.pysh_tree.PyshTreeNode()
    tree.loadFromList(t)
    tree.remove_ultra_padding()
    return tree.toList()

def list_to_open_close_sequence(lst):
    newList = [':open']
    for e in lst:
        if type(e) == list:
            newList += list_to_open_close_sequence(e)
        else:
            newList += [e]
    newList += [':close']
    return newList

#print list_to_open_close_sequence([1, 2, ['a', 'b',['c'],[['d']],'e']])

def open_close_sequence_to_list(lst):
    pyString = ''
    for element in lst:
        if element == ':open':
            pyString += '['
        elif element == ':close':
            pyString += ']'
            pyString += ','
        else:
            pyString += str(element)
            pyString += ','
    pyString = pyString[:-1]
    
    errors = True
    progressIndex = 0
    while errors:
        try: pyCode = eval(pyString)
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
    return list(pyCode)

'''
#newList = open_close_sequence_to_list([':open', 1, 2, ':open', 'a', 'b', ':open', 'c', ':close', ':open', ':open', 'd', ':close', ':close', 'e', ':close', ':close'])
newList = open_close_sequence_to_list([':open', 1, ':close', ':open', 2, ':close'])
print newList
'''

def insert_somewhere(thing, lst):
    after_how_many = Pysh.random_push.lrand_int(len(lst)+1)
    l = list(lst[:after_how_many])
    l += [thing]
    l += lst[after_how_many:]
    return l
#print insert_somewhere('HIT', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def delete_somewhere(thing, lst):
    locations = []
    for i  in range(len(lst)):
        if lst[i] == thing:
            locations.append(i)
    location = Pysh.random_push.lrand_nth(locations)
    newList = lst[:location +1] + lst[location:]
    return newList

def left_balence(s, left, right):
    processed = []
    to_process = s
    extra_lefts = 0
    while len(to_process)>0:
        #print processed
        if to_process[0] == left:
            processed += [to_process[0]]
            to_process.remove(to_process[0])
            extra_lefts += 1
        elif to_process[0] == right:
            if extra_lefts == 0:
                if Pysh.random_push.lrand()<0.5:
                    to_process = delete_somewhere(right, processed + [right]) + to_process[1:]
                    extra_lefts = 0
                    processed = []
                else:
                    to_process = insert_somewhere(left, processed) + to_process
                    extra_lefts = 0
                    processed = []
            else:
                processed = processed + [to_process[0]]
                to_process.remove(to_process[0])
                extra_lefts -= 1
        else:
            processed = processed + [to_process[0]]
            to_process.remove(to_process[0])
    return processed

def balance(open_close_sequence):
    open_close_sequence = left_balence(open_close_sequence, ':open', ':close')
    open_close_sequence.reverse()
    open_close_sequence = left_balence(open_close_sequence, ':close', ':open')
    open_close_sequence.reverse()
    return open_close_sequence
'''  
l = [':open', 1, 2, ':open', 'a', 'b', ':open', 'c', ':close', ':close', ':open', ':open', 'd', ':close', ':close', 'e', ':close', ':close']
print l
print balance(l)  
'''
'''
l = [':open', ':open', ':close']
#print open_close_sequence_to_list(l)
print l
print balance(l)  
'''

def alternate(s1, s2, alternation_rate, alignment_deviation):
    s1 = list(s1)
    s2 = list(s2)
    
    i = 0
    use_s1 = Pysh.random_push.lrand_nth([True, False])
    result = []
    looping = True
    while looping:
        if use_s1:
            temp = s1
        else:
            temp = s2
        if i >= len(temp) or len(result) > 10000:
            looping = False
        else:
            if Pysh.random_push.lrand() < alternation_rate:
                if round(gaussian_noise_factor() * alignment_deviation, 0) + i > 0:
                    i = int(round(gaussian_noise_factor() * alignment_deviation, 0) + i)
                else:
                    i = 0
                use_s1 = not use_s1
            else:
                if use_s1:
                    result.append(s1[i])
                else:
                    result.append(s2[i])
                i += 1
    return result
'''
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print alternate(l1, l2, 0.2, 1)
'''

def linearly_mutate(open_close_sequence, mutation_rate, use_ultra_no_paren_mutation, atom_generators):
    if Pysh.globals.global_use_bushy_code:
        n = len(atom_generators)
        parentheses = ([':open']*n) + ([':close']*n)
    else:
        parentheses = [':open', ':close']
    
    def token_mutator(token):
        if  ((not use_ultra_no_paren_mutation) or (token != ':open' and token != ':close') and (Pysh.random_push.lrand() < mutation_rate)):
            if use_ultra_no_paren_mutation:
                return Pysh.random_push.random_code(1, atom_generators)
            else:
                return Pysh.random_push.random_code(1, atom_generators+parentheses)
        else:
            return token
    ret = []
    for e in open_close_sequence:
        ret.append(token_mutator(e))
    return ret

def ultra_operate_on_programs(p1, p2, alternation_rate, alignment_deviation, mutation_rate, use_ultra_no_paren_mutation, ultra_pads_with_empties, atom_generators):
    pass