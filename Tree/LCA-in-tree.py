'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    def lca(self,root, n1, n2):
        if root is None or root.data==n1 or root.data==n2:
            return root
        
        left=self.lca(root.left,n1,n2)
        right=self.lca(root.right,n1,n2)
        
        if left is None:
            return right
        elif right is None:
            return left
        else: #if boot left and right both are not null then the root is ans
            return root