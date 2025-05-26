class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        n=len(arr)
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            
            if arr[low]<=arr[mid]:
                ans=min(ans,arr[low])
                low=mid+1
            
            else:
                high=mid-1
                ans=min(ans,arr[mid])
                
                
        return ans