class Solution:

	def nthRowOfPascalTriangle(self, n):
	    row=[1]
	    res=1
	    for i in range(1,n):
	        res=res*(n-i)
	        res=res//i
	        row.append(res)
	        
	    return row