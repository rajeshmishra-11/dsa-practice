from collections import defaultdict
class Solution:
    def countPaths(self, V, edges):
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        path=[0]*V
        min_time=[float('inf')]*V
        min_time[0]=0
        path[0]=1
        
        pq=[(0,0)]
        
        while pq:
            cur_time,node=heapq.heappop(pq)
            
            if cur_time>min_time[node]:
                continue
            
            for next_node,next_time in adj[node]:
                
                new_time=next_time+cur_time
                
                if new_time<min_time[next_node]:
                    min_time[next_node]=new_time
                    path[next_node]=path[node]
                    heapq.heappush(pq,(new_time,next_node))
                    
                elif new_time==min_time[next_node]:
                    path[next_node]=path[node]+path[next_node]
                    
        return path[V-1]