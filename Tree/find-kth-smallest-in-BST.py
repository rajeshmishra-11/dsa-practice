'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        cnt=0
        curr=root
        
        while curr:
            
            if not curr.left:
                cnt+=1
                
                if cnt==k:
                    return curr.data
                
                curr=curr.right
            
            else:
                prev=curr.left
                while prev.right and prev.right != curr:
                    prev=prev.right
                    
                if not prev.right:
                    prev.right=curr
                    curr=curr.left
                    
                else:
                    prev.right=None
                    cnt+=1
                    
                    if cnt==k:
                        return curr.data
                        
                        
                    curr=curr.right
                    
            
        return -1