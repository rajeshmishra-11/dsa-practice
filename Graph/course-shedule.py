class Solution:
    
    def dfs(self,node,vis,stack,adj):
        
        vis[node]=1
        
        for neighbor in adj[node]:
            if vis[neighbor]==1:
                return False
                
            elif vis[neighbor]==0:
                if not self.dfs(neighbor,vis,stack,adj):
                    return False
        vis[node]=2            
        stack.append(node)
        return True
    
    def findOrder(self, n, prerequisites):
        adj=[[] for _ in range(n)]
        for i,j in prerequisites:
            adj[j].append(i)
            
        visited=[0]*n
        stack=[]
        
        for i in range(n):
            if visited[i]==0:
                if not self.dfs(i,visited,stack,adj):
                    return []
                    
        stack.reverse()           
        return stack