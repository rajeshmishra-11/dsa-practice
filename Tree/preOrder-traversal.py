
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def preorder(self,root):
        if root is None:
            return []
        res=[root.data]
        res+=self.preorder(root.left)
        res+=self.preorder(root.right)
        return res