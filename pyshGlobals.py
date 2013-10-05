'''
Created on Oct 2, 2013

@author: Eddie
'''

class Exec(object):
    symbol = None
    def __init__(self, sym):
        self.symbol = sym

def random(typ, min = None, max = None):
    if typ is int:
        return random(min, max)
    elif type is Exec:
        

pysh_types = [int, float, Exec]