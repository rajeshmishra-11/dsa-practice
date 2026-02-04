from collections import defaultdict
from collections import deque

class Solution:
    def shortestPath(self, V, edges, src):
        
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        dist=[float('inf')]*V
        dist[src]=0
        
        q=deque()
        
        q.append(src)
        while q:
            node=q.popleft()
            for i in adj[node]:
                if dist[node]+1<dist[i]:
                    dist[i]=dist[node]+1
                    q.append(i)
                    
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i]=-1
                
        return dist