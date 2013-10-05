 '''
Created on Oct 2, 2013

@author: Eddie
'''
import pyshState

class PyshInterpreter(object):
    '''
    classdocs
    '''
    state = None

    def __init__(self):
        '''
        Constructor
        '''
        self.state = pyshState.PyshState()
        
        
    