#User function Template for python3

'''
# Node Class:
class Node:
    def init(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    
    def findLH(self,node):
        ht=0
        while node:
            node=node.left
            ht+=1
        return ht
        
    def findRH(self,node):
        ht=0
        while node:
            node=node.right
            ht+=1
        return ht
        
    
    def countNodes(self, root):
        if root is None:
            return 0
        
        lh=self.findLH(root)
        rh=self.findRH(root)
        
        if lh==rh:
            return 2**lh-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)