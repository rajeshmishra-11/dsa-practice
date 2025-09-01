'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def zigZagTraversal(self, root):
        res=[]
        if root is None:
            return res
        
        s1=[]
        s2=[]
        
        s1.append(root)
        
        while s1 or s2:
            
            while s1:
                cur=s1.pop()
                res.append(cur.data)
                
                if cur.left:
                    s2.append(cur.left)
                if cur.right:
                    s2.append(cur.right)
                    
            while s2:
                cur=s2.pop()
                res.append(cur.data)
                
                if cur.right:
                    s1.append(cur.right)
                
                if cur.left:
                    s1.append(cur.left)
                    
                
                
                
        return res