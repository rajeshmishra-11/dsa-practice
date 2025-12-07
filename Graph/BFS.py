class Solution:
    def bfs(self, adj):
        n=len(adj)
        res=[]
        visited=[False]*n
        q=deque()
        visited[0]=True
        q.append(0)
        
        while q:
            cur=q.popleft()
            res.append(cur)
            
            for i in adj[cur]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=True