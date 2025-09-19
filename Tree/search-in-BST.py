'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class BST:
    def search(self, node, x):
        while node:
            
            if node.data==x:
                return True
                
            if node.data>x:
                node=node.left
                
            elif node.data<x:
                node=node.right
                           
                
        return False