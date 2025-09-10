class Solution:
    
    def findTarNode(self,root,tar,parent):
        q=deque([root])
        tar_node=None
        
        while q:
            node=q.popleft()
            if node.data==tar:
                tar_node=node
            
            if node.left:
                parent[node.left]=node
                q.append(node.left)
                
            if node.right:
                parent[node.right]=node
                q.append(node.right)
        return tar_node
        
    
    def bfsburn(self,start,parents):
        q=deque([start])
        visited=set([start])
        time=0
        
        while q:
            n=len(q)
            flag=False
            for _ in range(n):
                node=q.popleft()
                
                if node.left and node.left not in visited:
                    flag=True
                    visited.add(node.left)
                    q.append(node.left)
                    
                    
                if node.right and node.right not in visited:
                    flag=True
                    visited.add(node.right)
                    q.append(node.right)
                    
                if node in parents and parents[node] not in visited:
                    flag=True
                    visited.add(parents[node])
                    q.append(parents[node])
                    
            if flag:
                time+=1
                
        return time
                    
    
    def minTime(self, root, target):
        
        parent={}
        start=self.findTarNode(root,target,parent)
        
        return self.bfsburn(start,parent)
        