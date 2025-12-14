
from typing import List

class Solution: 
    
    def dfs(self,grid,visited,row,col):
        if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col]==1 and not visited[row][col]:
            visited[row][col] = 1
            self.dfs(grid, visited, row + 1, col)
            self.dfs(grid, visited, row - 1, col)
            self.dfs(grid, visited, row, col + 1)
            self.dfs(grid, visited, row, col - 1)
    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        visited = [[0 for _ in range(m)] for _ in range(n)]

        
        for i in range(n):
            if not visited[i][0] and grid[i][0]==1:
                self.dfs(grid,visited,i,0)
                
            if not visited[i][m-1] and grid[i][m-1]==1:
                self.dfs(grid,visited,i,m-1)
                
        for j in range(m):
            if not visited[0][j] and grid[0][j]==1:
                self.dfs(grid,visited,0,j)
                
            if not visited[n-1][j] and grid[n-1][j]==1:
                self.dfs(grid,visited,n-1,j)
                
                
        cnt=0
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]==1:
                    cnt+=1
                    
        return cnt