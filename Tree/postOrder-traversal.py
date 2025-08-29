'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        if root is None:
            return []
        res=[]
        res+=self.postOrder(root.left)
        res+=self.postOrder(root.right)
        res+=[root.data]
        return res