'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def mirrorimage(self,left,right):
        if left==None or right==None:
            return left==right
        
        if left.data!=right.data:
            return False
        
        return self.mirrorimage(left.left,right.right) and self.mirrorimage(left.right,right.left)
    
    def isSymmetric(self, root):
        return root==None or self.mirrorimage(root.left,root.right)