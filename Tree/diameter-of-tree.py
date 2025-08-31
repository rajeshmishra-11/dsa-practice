'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def height(self,root,diameter):
        if root is None:
            return 0
        lh=self.height(root.left,diameter)
        rh=self.height(root.right,diameter)
        
        diameter[0]=max(diameter[0],lh+rh)
        
        return 1+max(lh,rh)
        
    
    def diameter(self, root):
        diameter=[0]
        self.height(root,diameter)
        return diameter[0]