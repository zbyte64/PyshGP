'''
Created on Sep 23, 2013

@author: Eddie
'''

class PyshController(object):
    '''
    classdocs
    '''
    int_Stack = None
    float_Stack = None
    string_Stack = None
    bool_Stack = None
    code_Stack = None
    
    def __init__(self):
        '''
        Constructor
        '''
        self.num_Stack= []
        self.char_Stack = []
        self.string_Stack = []
        self.bool_Stack = []
        self.code_Stack = []
        
    def push(self, stack, val):
        if stack == 'n':
            val = (float(val))
            self.num_Stack.append(val)
        elif stack == 's':
            self.string_Stack.append(val)
        elif stack == 'b':
            if val == 'true':
                self.bool_Stack.append(True)
            elif val == 'false':
                self.bool_Stack.append(False)
            else:
                self.bool_Stack.append("NOT BOOL VAL")
        elif stack == 'x':
            self.code_Stack.append(val)
        else:
            print("Non-Existent Stack to PUSH to")
            
    def pop(self, stack):
        if stack == 'n':
            return self.num_Stack.pop()
        elif stack == 's':
            return self.string_Stack.pop()
        elif stack == 'b':
            return self.bool_Stack.pop()
        elif stack == 'x':
            return self.code_Stack.pop()
        else:
            print("Non-Existent Stack to POP from")
    
    def print_stack(self, stack):
        print("<- In First, Out Last     In Last, Out First->")
        if stack == 'n':
            print(self.num_Stack)
        elif stack == 's':
            print(self.string_Stack)
        elif stack == 'b':
            print(self.bool_Stack)
        elif stack == 'x':
            print(self.code_Stack)
        else:
            print("Non-Existent Stack to PRINT")
            
    def print_all_stacks(self):
        print("<- In First, Out Last     In Last, Out First->")
        print("Nums: " + str(self.num_Stack))
        print("String: " + str(self.string_Stack))
        print("Bool: " + str(self.bool_Stack))
        print("Code: " + str(self.code_Stack))
        
    def add(self, stack1, stack2):
        var1 = self.pop(stack1)
        var2 = self.pop(stack2)
        if (type(var1) is int or type(var1) is float or type(var1) is str) and (type(var2) is int or type(var2) is float or type(var2) is str):
            if type(var1) is type(var2):
                self.push('n', (var1 + var2))
            else:
                self.push('s', (var1 + `var2`))
        else:
            pass
            
    def subtract(self, stack1, stack2):
        var1 = self.pop(stack1)
        var2 = self.pop(stack2)
        if stack1 == 'n' and stack2 == 'n':
            self.push('n', (var1-var2))
        else:
            print "Not valid subtraction move, nothing done."
            pass
    
    def multiply(self, stack1, stack2):
        var1 = self.pop(stack1)
        var2 = self.pop(stack2)
        if stack1 == 'n' and stack2 == 'n':
            self.push('n', (self.pop(stack1)*self.pop(stack2)))
        elif (stack1 == 's' and stack2 == 'n') or (stack1 == 'n' and stack2 == 's'):
            self.push('s', (self.pop(stack1)*self.pop(stack2)))
        else:
            pass
    
    def divide(self, stack1, stack2):
        if stack1 == 'n' and stack2 == 'n':
            self.push('n', (self.pop(stack1)/self.pop(stack2)))
        else:
            pass
        
    
        
        