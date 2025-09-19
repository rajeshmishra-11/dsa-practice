''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        ceil=-1
        while root:
            if root.data==x:
                return root.data
            elif root.data>x:
                ceil=root.data
                root=root.left
                
            else:
                root=root.right
                
        return ceil