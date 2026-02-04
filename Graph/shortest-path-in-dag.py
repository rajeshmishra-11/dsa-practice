from typing import List
from collections import defaultdict
import math


class Solution:

    def shortestPath(self, V: int, E: int,edges: List[List[int]]) -> List[int]:
        
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            
        visited=[False]*V
        stack=[]
        
        def dfs(node):
            visited[node]=True
            for neigh,wt in adj[node]:
                if not visited[neigh]:
                    dfs(neigh)
                    
            stack.append(node)
            
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        stack.reverse()
        
        dist=[math.inf]*V
        dist[0]=0
        
        for u in stack:
            if dist[u]!=math.inf:
                for v,wt in adj[u]:
                    if dist[u]+wt<dist[v]:
                        dist[v]=dist[u]+wt
                        
                        
        for i in range(V):
            if dist[i]==math.inf:
                dist[i]=-1
                
        return dist