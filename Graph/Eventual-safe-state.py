class Solution:
    
    def dfs(self,cur,visited,pathvis,safe,adj):
        visited[cur]=True
        pathvis[cur]=True
        safe[cur]=True
        
        for nexxt in adj[cur]:
            if not visited[nexxt]:
                if not self.dfs(nexxt,visited,pathvis,safe,adj):
                    safe[cur]=False
                    break
                
            elif pathvis[nexxt]:
                safe[cur]=False
                break
            
            elif not safe[nexxt]:
                safe[cur] = False
                break
            
        pathvis[cur]=False
        return safe[cur]
    
    def safeNodes(self, V, edges):
        visited=[False]*V
        pathvis=[False]*V
        safe=[False]*V
        ans=[]
        
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        for i in range(V):
            if not visited[i]:
                self.dfs(i,visited,pathvis,safe,adj)
                
                
        for i in range(V):
            if safe[i]:
                ans.append(i)
                
        return ans