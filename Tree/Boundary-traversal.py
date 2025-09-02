'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def isleaf(self,root):
        return root.left is None and root.right is None
        
    def collectleftboundary(self,root,res):
        if root is None or self.isleaf(root):
            return 
        
        res.append(root.data)
        if root.left:
            self.collectleftboundary(root.left,res)
        else:
            self.collectleftboundary(root.right,res)
            
    def collectleaf(self,root,res):
        if root is None:
            return 
        
        if self.isleaf(root):
            res.append(root.data)
            return 
        if root.left:
            self.collectleaf(root.left,res)
        if root.right:
            self.collectleaf(root.right,res)
        
    def collectrightboundary(self,root,res):
        if root is None or self.isleaf(root):
            return
        if root.right:
            self.collectrightboundary(root.right,res)
        else:
            self.collectrightboundary(root.left,res)
            
        res.append(root.data)
    
    def boundaryTraversal(self, root):
        res=[]
        if not root:
            return res

        if not self.isleaf(root):
            res.append(root.data)

        self.collectleftboundary(root.left,res)


        self.collectleaf(root,res)

        self.collectrightboundary(root.right,res)

        return res