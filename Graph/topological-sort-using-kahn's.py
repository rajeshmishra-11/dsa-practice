from collections import deque
class Solution:
        
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        indegree=[0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
                
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                
        topo=[]
        while q:
            node=q.pop()
            topo.append(node)
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it]==0:
                    q.append(it)
                    
                    
        return topo