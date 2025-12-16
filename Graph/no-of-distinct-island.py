
import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    
    def dfs(self,grid,x0,y0,i,j,v):
        
        dirs=[[0,-1],[-1,0],[1,0],[0,1]]
        
        rows=len(grid)
        cols=len(grid[0])
        
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
            return 
        
        grid[i][j]=-1
        
        v.append((i-x0,j-y0))
        
        for dir in dirs: 
            self.dfs(grid, x0, y0, i + dir[0], j + dir[1], v)

        
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        rows=len(grid)
        
        if rows==0:
            return 0
            
        cols=len(grid[0])
        
        if cols==0:
            return 0
            
        cordinates=set()
        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j]!=1:
                    continue
                
                v=[]
                self.dfs(grid,i,j,i,j,v)
        
                cordinates.add(tuple(v))
        
        return len(cordinates)