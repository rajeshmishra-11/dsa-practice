'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isbst(self,root,minm,maxm):
        if root is None:
            return True
            
        if root.data>maxm or root.data<minm:
            return False
            
        return (self.isbst(root.left,minm,root.data-1) and self.isbst(root.right,root.data+1,maxm))
        
    def isBST(self, root):
            
        minm=float('-inf')
        maxm=float('inf')
            
        return self.isbst(root,minm,maxm)