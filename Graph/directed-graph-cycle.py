class Solution:
    
    def find_cycle(self,adj,u,vis,path):
        if path[u]:
            return True
            
        if vis[u]:
            return False
            
        vis[u]=True
        path[u]=True
        
        for v in adj[u]:
            if self.find_cycle(adj,v,vis,path):
                return True
                
        path[u]=False
        return False
            
            
    
    def isCyclic(self, V, edges):
        visited=[False]*V
        path=[False]*V
        
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            
        for i in range(V):
            if not visited[i] and self.find_cycle(adj,i,visited,path):
                return True
                
        return False