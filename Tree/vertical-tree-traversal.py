from collections import defaultdict
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def verticalOrder(self, root): 
        mp=defaultdict(list)
        hd=0
        
        q=deque([(root,0)])
        
        mx=0
        mn=0
        
        while q:
            node,hd=q.popleft()
            
            mp[hd].append(node.data)
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
            
            mx=max(mx,hd)
            mn=min(mn,hd)

        res=[]
        for i in range(mn,mx+1):
            res.append(mp[i])
            
        return res
            