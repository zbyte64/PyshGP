'''
Created on Oct 2, 2013

@author: Eddie
'''
class Exec(object):
    symbol = None
    def __init__(self, sym):
        self.symbol = sym


pysh_types = [int, float, Exec]