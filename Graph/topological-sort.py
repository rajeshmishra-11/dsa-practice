class Solution:
    
    def dfs(self,node,adj,st,vis):
        vis[node]=1
        for it in adj[node]:
            if vis[it]==0:
                self.dfs(it,adj,st,vis)
            
        st.append(node)
        
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        st=[]
        vis=[0]*V
        
        for i in range(V):
            if vis[i]==0:
                self.dfs(i,adj,st,vis)
        
        ans=[]        
        while st:
            ans.append(st.pop())
            
        return ans