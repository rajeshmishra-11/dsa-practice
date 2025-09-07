from collections import deque
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxWidth(self, root):
        if root is None:
            return 0
        ans=0
        q=deque([root])
        while q:
            n=len(q)
            ans=max(ans,n)
            for i in range(n):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            
        return ans