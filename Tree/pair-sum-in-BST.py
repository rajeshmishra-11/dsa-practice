'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    
    def inorder_traversal(self,root,inorder):
        
        if root is None:
            return 
        
        self.inorder_traversal(root.left,inorder)
        
        inorder.append(root.data)
        
        self.inorder_traversal(root.right,inorder)
    
    def findTarget(self, root, target): 
        
        inorder=[]
        
        self.inorder_traversal(root,inorder)
        
        left=0
        right=len(inorder)-1
        
        while left<right:
            cursum=inorder[left]+inorder[right]
            
            if cursum==target:
                return True
                
            elif cursum<target:
                left+=1
            else:
                right-=1
        return False