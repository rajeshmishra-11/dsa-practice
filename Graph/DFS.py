class Solution:
    def dfsrec(self,adj,visited,res,s):
        visited[s]=True
        res.append(s)
        
        for i in adj[s]:
            if not visited[i]:
                self.dfsrec(adj,visited,res,i)
                
    def dfs(self, adj):
        visited=[False]*len(adj)
        res=[]
        self.dfsrec(adj,visited,res,0)
        return res