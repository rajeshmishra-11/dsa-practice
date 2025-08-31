'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def max_sum_path(self,root,maxi):
        if root is None:
            return 0
        lsum=max(0,self.max_sum_path(root.left,maxi))
        rsum=max(0,self.max_sum_path(root.right,maxi))
        
        maxi[0]=max(maxi[0],root.data+lsum+rsum)
        
        return root.data+max(lsum,rsum)
    
    def findMaxSum(self, root): 
        maxi=[float('-inf')]
        self.max_sum_path(root,maxi)
        return maxi[0]