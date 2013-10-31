'''
Created on Oct 26, 2013

@author: Eddie
'''

def foo(val):
    def bar(num):
        return val + num
    return bar

f = foo(5)
print f(10)

g = foo(25)
print g(50)