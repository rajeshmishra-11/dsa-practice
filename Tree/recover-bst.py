'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def correctbstUntil(self,root,first,last,middle,prev):
        if root is None:
            return
        
        self.correctbstUntil(root.left,first,last,middle,prev)
        
        if prev[0] and root.data<prev[0].data:
            
            if not first[0]:
                first[0]=prev[0]
                middle[0]=root
                
            else:
                last[0]=root
                
        prev[0]=root
        
        self.correctbstUntil(root.right,first,last,middle,prev)
    
    def correctBST(self, root):
        first,last,middle,prev=[None],[None],[None],[None]
        
        self.correctbstUntil(root,first,last,middle,prev)
        
        if first[0] and last[0]:
            first[0].data,last[0].data=last[0].data,first[0].data
            
        elif first[0] and middle[0]:
            first[0].data,middle[0].data=middle[0].data,first[0].data