class Solution:
    def searchInsertK(self, Arr, N, k):
        ans=N
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            
            if Arr[mid]>=k:
                ans=mid
                high=mid-1
            
            else:
                low=mid+1
        
        return ans