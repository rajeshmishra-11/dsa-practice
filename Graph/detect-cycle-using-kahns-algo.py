from collections import deque
class Solution:
    def isCyclic(self, V, edges):
        # solve the problem using the kahn's Algorithm
        
        adj=[[]for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            
        indegree=[0]*V
        q=deque()
        for i in range(V):
            for next_val in adj[i]:
                indegree[next_val]+=1
                
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        cnt=0        
        while q:
            top=(q.popleft())
            cnt+=1
            for i in adj[top]:
                indegree[i]-=1
                if indegree[i] ==0:
                    q.append(i)
                    
                    
        if cnt==V:
            return False
        
        return True   