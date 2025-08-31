'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def maxDepth(self, root):
        if root is None:
            return 0
        lh=self.maxDepth(root.left)
        if lh==-1:
            return -1
        rh=self.maxDepth(root.right)
        if rh==-1:
            return -1
            
        if (abs(lh-rh)>1):
            return -1
        
        return 1+max(lh,rh)
    
    def isBalanced(self, root):
        if self.maxDepth==-1:
            return False
        else:
            return True