'''
Created on Oct 2, 2013

@author: Eddie

This class is used in place of Clojush's instruction files, and made into a more OOP system

Each stack holds the instructions for handling the elements, and the instructions themselves are not added to the Exec stack,
Instead, each function is mapped to a symbol ( convention $(function initials) ) and these symbols are pushed to the Exec stack.
'''
class PyshStack(object):
    '''
    Super-class for all stacks
    '''
    def __init__(self):
        self.stack = []
        
    def get_stack(self):
        return self.stack

class Number_Instructions(PyshStack):

    def __init__(self):
        PyshStack.__init__(self)
        
    def adder(self):
        '''
        symbol: $nia
        '''
        if len(self.stack) > 1:
            self.stack.append(self.stack.pop() + self.stack.pop())
        else:
            print("not enough numbers to add")
            
    def subtracter(self):
        '''
        symbol: $nis
        '''
        if len(self.stack) > 1:
            self.stack.append(self.stack.pop() - self.stack.pop())
        else:
            print('not enough numbers to subtract')
            
    def multiplier(self):
        '''
        symbol: $nim
        '''
        if len(self.stack) > 1:
            self.stack.append(self.stack.pop() * self.stack.pop())
        else:
            print('not enough numbers to multiply')
     
    def divider(self):
        '''
        symbol: $nid
        '''
        if len(self.stack) > 1:
            temp1 = self.stack.pop()
            temp2 = self.stack.pop()
            if temp2 != 0:
                self.stack.append(temp1 / temp2)
        else:
            print('not enough numbers to divide')
    
    def modder(self):
        '''
        symbol: $nimd
        '''
        if len(self.stack) > 1:
            temp1 = self.stack.pop()
            temp2 = self.stack.pop()
            if temp2 != 0:
                self.stack.append(temp1 % temp2)
        else:
            print('not enough numbers to find modulus')   
    
    def lessthaner(self):
        '''
        symbol: $nilt
        
        How to make this function push to the boolean stack in an efficient way
        '''
        pass
    
    def greaterthaner(self):
        '''
        symbol: $nigt
        
        How to make this function push to the boolean stack in an efficient way
        '''
        pass
    
    def minner(self):
        '''
        symbol: $nimin
        '''
        if len(self.stack) > 1:
            self.stack.append(min(self.stack.pop(), self.stack.pop()))
        else:
            print('not enough numbers to find min')
            
    def maxer(self):
        '''
        symbol: $nimax
        '''
        if len(self.stack) > 1:
            self.stack.append(max(self.stack.pop(), self.stack.pop()))
        else:
            print('not enough numbers to find max')