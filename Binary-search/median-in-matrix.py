class Solution:
    def upperBound(self, arr, target):
        n=len(arr)
        ans=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]>target:
                ans=mid
                high=mid-1
            
            else:
                low=mid+1
        
        return ans
    
    
    def count_lower_val(self,mat,n,m,x):
        cnt=0
        for i in range(n):
            cnt+=self.upperBound(mat[i],x)
        return cnt
    
    def median(self, mat):
    	n=len(mat)
    	m=len(mat[0])
    	low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
    	    
    	req=(n*m)//2
    	while low<=high:
    	    mid=(low+high)//2
    	    smallequal=self.count_lower_val(mat,n,m,mid)
    	    if smallequal<=req:
    	        low=mid+1
    	    else:
    	        high=mid-1
    	return low