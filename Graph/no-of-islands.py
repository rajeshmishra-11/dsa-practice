from collections import deque
class Solution:
    
    def issafe(self,grid,r,c,visited):
        n=len(grid)
        m=len(grid[0])
        return (0 <= r < n and 0 <= c < m and grid[r][c] == 'L' and not visited[r][c])

    
    def dfs(self,grid,visited,sr,sc):
        
        dRow = [-1, -1, -1, 0, 0, 1, 1, 1]
        dCol = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        q=deque()
        q.append((sr,sc))
        visited[sr][sc]=True
        
        while q:
            r,c=q.popleft()
            
            for k in range(8):
                newr=r+dRow[k]
                newc=c+dCol[k]
                if self.issafe(grid,newr,newc,visited):
                    visited[newr][newc]=True
                    q.append((newr,newc))
                    
            
    
    def numIslands(self, grid):
        n=len(grid)
        m=len(grid[0])
        visited = [[False] * m for _ in range(n)]
        islands=0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c]=='L' and not visited[r][c]:
                    self.dfs(grid,visited,r,c)
                    islands+=1
                    
        return islands