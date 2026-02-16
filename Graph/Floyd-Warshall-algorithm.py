class Solution:
	def floydWarshall(self, dist):
		n=len(dist)
		
		for i in range(n):
		    for j in range(n):
		        for k in range(n):
		            
		            if dist[j][i]!=100000000 and dist[i][k]!=100000000:
		                dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])
		                
		return dist