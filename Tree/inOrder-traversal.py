'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        if root is None:
            return []
        res=[]
        res+=self.inOrder(root.left)
        res+=[root.data]
        res+=self.inOrder(root.right)
        return res