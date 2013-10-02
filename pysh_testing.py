'''
Created on Sep 24, 2013

@author: Eddie
'''

from Pysh import PyshController
from pysh_repl import Pysh_Repl

pc = PyshController()

pc.push('i', 5)
pc.push('i', 100)
pc.push('i', -7)
pc.push('i', 44)
pc.pop('i')

pc.push('s', "Hello")
pc.push('s', "World")

pc.push('f', 2.5)

pc.print_all_stacks()

print
print

pc.add('i', 'f', 'f')
pc.multiply('i', 'i', 'i')

pc.print_all_stacks()