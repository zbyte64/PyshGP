'''
Created on Oct 2, 2013

@author: Eddie

This class is used in place of Clojush's instruction files, and made into a more OOP system

Each stack holds the instructions for handling the elements, and the instructions themselves are not added to the Exec stack,
Instead, each function is mapped to a symbol ( convention $(function initials) ) and these symbols are pushed to the Exec stack.
'''
class PyshStack(list):
    '''
    Super-class for all stacks
    '''
    def __init__(self):
        self = []
        
    def get_stack(self):
        return self

class Number_Instructions(PyshStack):

    def __init__(self):
        PyshStack.__init__(self)
        
    def adder(self):
        '''
        symbol: $nia
        '''
        if len(self) > 1:
            self.append(self.pop() + self.pop())
        else:
            print("not enough numbers to add")
            
    def subtracter(self):
        '''
        symbol: $nis
        '''
        if len(self) > 1:
            self.append(self.pop() - self.pop())
        else:
            print('not enough numbers to subtract')
            
    def multiplier(self):
        '''
        symbol: $nim
        '''
        if len(self) > 1:
            self.append(self.pop() * self.pop())
        else:
            print('not enough numbers to multiply')
     
    def divider(self):
        '''
        symbol: $nid
        '''
        if len(self) > 1:
            temp1 = self.pop()
            temp2 = self.pop()
            if temp2 != 0:
                self.append(temp1 / temp2)
        else:
            print('not enough numbers to divide')
    
    def modder(self):
        '''
        symbol: $nimd
        '''
        if len(self) > 1:
            temp1 = self.pop()
            temp2 = self.pop()
            if temp2 != 0:
                self.append(temp1 % temp2)
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
        if len(self) > 1:
            self.append(min(self.pop(), self.pop()))
        else:
            print('not enough numbers to find min')
            
    def maxer(self):
        '''
        symbol: $nimax
        '''
        if len(self) > 1:
            self.append(max(self.pop(), self.pop()))
        else:
            print('not enough numbers to find max')