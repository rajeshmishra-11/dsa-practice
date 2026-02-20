class Solution:
    def spanningTree(self, V, edges):
        
        adj=[[]for _ in range(V)]
        
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        pq=[]
        visited=[False]*V
        
        heapq.heappush(pq,(0,0))
        res=0
        
        while pq:
            
            wt,u=heapq.heappop(pq)
            
            if visited[u]:
                continue
            
            res+=wt
            visited[u]=True
            
            for v in adj[u]:
                if not visited[v[0]]:
                    heapq.heappush(pq,(v[1],v[0]))
                    
                    
        return res