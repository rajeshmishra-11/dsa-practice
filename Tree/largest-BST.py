import sys
class BSTinfo:
    def __init__(self,min_val,max_val,max_size):
        self.min=min_val
        self.max=max_val
        self.maxsize=max_size
        
        
        
        
class Solution:
    
    def largestBSTBT(self, root):
        
        if not root:
            return BSTinfo(sys.maxsize,-sys.maxsize-1,0)
            
            
        left=self.largestBSTBT(root.left)
        right=self.largestBSTBT(root.right)
        
        if left.max<root.data<right.min:
            return BSTinfo(min(left.min,root.data),max(right.max,root.data),1+left.maxsize+right.maxsize)
            
        return BSTinfo(-sys.maxsize - 1, sys.maxsize, max(left.maxsize, right.maxsize))
    
    
    def largestBst(self, root):
        return self.largestBSTBT(root).maxsize