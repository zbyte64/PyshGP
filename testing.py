'''
Created on Oct 26, 2013

@author: Eddie
'''

fs = []
fs.append(lambda x: x**2)
fs.append(lambda x: x**3)

for i in range(3):
    print(fs[0](i))
    print(fs[1](i))
    print