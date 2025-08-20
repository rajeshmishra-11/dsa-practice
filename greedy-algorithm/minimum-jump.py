class Solution:
	def minJumps(self, arr):
	    jump=0
	    n=len(arr)
	    if arr[0]==0:
	        return -1
	        
	    l=0
	    r=0
	    while r<n-1:
	       forward=0
	       for i in range(l,r+1):
	           forward=max(i+arr[i],forward)
	       if forward<=r:
	           return -1
	       l=r+1
	       r=forward
	       jump+=1
	    
	    return jump