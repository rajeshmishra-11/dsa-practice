#User function Template for python3

from typing import List

class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        dist=[[float('inf')]*n for _ in range(n)]
        
        for i in range(n):
            dist[i][i]=0
        
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
            
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
                    
                    
        min_cnt=float('inf')
        ans=-1
        
        for city in range(n):
            cnt=0
            for adj in range(n):
                if dist[city][adj]<=distanceThreshold:
                    cnt+=1
                    
            if cnt<=min_cnt:
                min_cnt=cnt
                ans=city
                
        return ans