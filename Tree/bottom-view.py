'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        if root is None:
            return []
        q=deque()
        mp={}
        q.append((root,0))
        
        while q:
            temp,hd=q.popleft()
            mp[hd]=temp.data
                
            if temp.left:
                q.append((temp.left,hd-1))
            if temp.right:
                q.append((temp.right,hd+1))
               
        ans = [mp[key] for key in sorted(mp.keys())]
            
        return ans