'''
Created on Dec 31, 2013

@author: Eddie Pantridge Hampshire College
'''

class PyshTreeNode(object):

    def __init__(self):
        self.children = []
        self.data = None
        self.parent = None
    
    def loadFromList(self, l):
        for e in l:
            if type(e) == list:
                n = PyshTreeNode()
                n.loadFromList(e)
                n.parent = self
                self.children.append(n)
            else:
                n = PyshTreeNode()
                n.data = e
                n.parent = self
                self.children.append(n)
    
    def toList(self):
        l = []
        if len(self.children)>0:
            for c in self.children:
                if type(c) == PyshTreeNode:
                    l.append(c.toList())
                else:
                    l.append(c)
            return l
        else:
            if self.data == None:
                return []
            else:
                return self.data
    
    def printNode(self, depth = 0):
        print ('\t'*depth) + '## Node: ##'
        if self.data != None:
            print ('\t'*depth) + 'Data: '+ str(self.data)
        if len(self.children)>0:
            print ('\t'*depth) + 'Children:'
            for c in self.children:
                if type(c) == PyshTreeNode:
                    c.printNode(depth+1)
                else:
                    print ('\t'*depth) + str(c)
        else:
            print ('\t'*depth) + 'No Children'
    
    def traverse(self, dir, ind = 0):
        if dir == 'up':
            return self.parent
        elif dir == 'down':
            return self.children[ind]
        elif dir == 'right':
            i = self.parent.children.index(self)
            return self.parent.children[i+1]
        elif dir == 'left':
            i = self.parent.children.index(self)
            return self.parent.children[i-1]
        
    def remove_empty_elements(self):
        if len(self.children) == 0 and self.data == None:
            self.parent.children.remove(self)
            return True
        else:
            for c in self.children:
                b = c.remove_empty_elements()
                if b:
                    b = self.remove_empty_elements()
    
    def remove_ultra_padding(self):
        if self.data == 'ultra-padding':
            self.parent.children.remove(self)
            return True
        else:
            for c in self.children:
                b = c.remove_ultra_padding()
                if b:
                    b = self.remove_ultra_padding()

#TESTING THE TREE
'''
t = PyshTreeNode()      
t.loadFromList([[7,[9,8],2,'ultra-padding',[5,[1,10],'ultra-padding']]])
t.remove_ultra_padding()
print t.toList()
'''
'''
currentNode = t
currentNode = currentNode.traverse('down')
currentNode = currentNode.traverse('down', 1)
currentNode.printNode()
print
print
currentNode = currentNode.traverse('up')
currentNode = currentNode.traverse('right')
currentNode.printNode()
print
print
l = t.toList()
print l
'''