class Solution:
    def isBipartite(self, V, edges):
        
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        color=[-1]*V
        
        for i in range(V):
            if color[i]==-1:
                color[i]=0
                q=deque([i])
                
                while q:
                    u=q.popleft()
                
                    for v in adj[u]:
                        if color[v]==-1:
                            color[v]=1-color[u]
                            q.append(v)
                        
                        elif color[v]==color[u]:
                            return False
                        
                        
        return True