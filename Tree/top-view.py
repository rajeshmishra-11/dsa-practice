from queue import Queue
# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return []
            
        temp=None
        
        mp={}
        
        q=Queue()
        
        mn=float('inf')
        q.put((root,0))
        
        while not q.empty():
            temp,d=q.get()
            
            mn=min(mn,d)
            
            if d not in mp:
                mp[d]=temp.data
                
            if temp.left:
                q.put((temp.left,d-1))
            if temp.right:
                q.put((temp.right,d+1))
                
        ans=[0]*len(mp)       
        for d,val in mp.items():
            ans[d-mn]=val
            
        return ans