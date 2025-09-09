'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def findTarNode(self,root,target,parent):
        
        if root.data==target:
            return root
        
        if root.left is not None:
            parent[root.left]=root
            left=self.findTarNode(root.left,target,parent)
            if left:
                return left
            
        if root.right is not None:
            parent[root.right]=root
            right=self.findTarNode(root.right,target,parent)
            if right:
                return right
                
            
    def dfs(self,root,prev,k,parent,ans):
        if not root:
            return 
        
        if k==0:
            ans.append(root.data)
            return 
            
        if root.left!=prev:
            self.dfs(root.left,root,k-1,parent,ans)
            
        if root.right!=prev:
            self.dfs(root.right,root,k-1,parent,ans)
            
        if parent.get(root) and parent[root] != prev:
            self.dfs(parent[root], root, k-1, parent, ans)
            
        return None
            
        
            
    def KDistanceNodes(self,root,target,k):
        ans=[]
        if not root:
            return ans
        
        parent={}
        parent[root]=None
        tar=self.findTarNode(root,target,parent)
        
        if not tar:
            return ans
        
        self.dfs(tar,None,k,parent,ans)
        
        ans.sort()

        
        return ans