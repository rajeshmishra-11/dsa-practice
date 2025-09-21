'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        if root is None:
            return None
        curr=root.data    
        if curr<n1.data and curr<n2.data:
            return self.LCA(root.right,n1,n2)
            
        if curr>n1.data and curr>n2.data:
            return self.LCA(root.left,n1,n2)
            
        return root
        