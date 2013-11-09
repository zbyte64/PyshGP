'''
Created on Oct 26, 2013

@author: Eddie
'''
import re

def foo(val):
    def bar(num):
        return val + num
    return bar

f = foo(5)
print f(10)

g = foo(25)
print g(50)


p = re.compile(r'[^\d-]*(-?[\d]+(\.[\d]*)?([eE][+-]?[\d]+)?)')
def string_atoi(input):
    m = p.match(input)
    if m:
        result = m.groups()[0]
        if "." in result or "e" in result or "E" in result:
            ret = "{1}".format(input, float(result))
        else:
            ret = '{1}'.format(input, int(result))
    return ret
    
print string_atoi('123big')
print string_atoi('1e5')
print string_atoi('$156')