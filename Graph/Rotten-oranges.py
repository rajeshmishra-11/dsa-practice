class Solution:
    
    def issafe(self,i,j,n,m):
        return 0<=i<n and 0<=j<m
    
	def orangesRot(self, mat):
		n=len(mat)
		m=len(mat[0])
		q=deque()
		time=0
		for i in range(n):
		    for j in range(m):
		        if mat[i][j]==2:
		            q.append((i,j))
		            
		direction=[(1,0),(0,1),(-1,0),(0,-1)]
		
		while q:
		    size=len(q)
		    flag=False
		    
		    for _ in range(size):
		        x,y=q.popleft()
		        
		        for dx,dy in direction:
		            nx,ny=x+dx,y+dy
		            
		            if self.issafe(nx,ny,n,m) and mat[nx][ny]==1:
		                mat[nx][ny]=2
		                q.append((nx,ny))
		                flag=True
		                
		                
		    if flag:
		        time+=1
		        
		        
	    for i in range(n):
	        for j in range(m):
	            if mat[i][j]==1:
	                return -1
	                
	    return time 