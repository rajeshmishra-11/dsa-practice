'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
            
    def deleteNode(self, root, x):
        
        if root is None:
            return root
            
        elif root.data<x:
            root.right=self.deleteNode(root.right,x)
            
            
        elif root.data>x:
            root.left=self.deleteNode(root.left,x)
            
            
        else:
            if root.left is None:
                return root.right
                
            elif root.right is None:
                return root.left
                
            else:
                temp=root.right
                while temp.left is not None:
                    temp=temp.left
                    
                root.data=temp.data
                
                root.right=self.deleteNode(root.right,temp.data)
                
                
        return root