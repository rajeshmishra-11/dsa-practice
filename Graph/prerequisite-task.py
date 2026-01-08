class Solution:
    
    def dfs(self,node,adj,vis):
        vis[node]=1
        
        for neighbor in adj[node]:
            if vis[neighbor]==1:
                return False
            
            if vis[neighbor]==0:
                if not self.dfs(neighbor,adj,vis):
                    return False
                    
        vis[node]=2
        return True
                
        
    
    def isPossible(self,N,P,prerequisites):
        adj=[[] for _ in range(N)]
        for i,j in prerequisites:
            adj[j].append(i)
            
        visited=[0]*N
        
        for i in range(N):
            if visited[i]==0:
                if not self.dfs(i,adj,visited):
                    return False
                    
        return True