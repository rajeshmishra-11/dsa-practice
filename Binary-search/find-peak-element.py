class Solution:   
    def peakElement(self,arr):
        n=len(arr)
        if n==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[n-1]>arr[n-2]:
            return n-1
            
        low=1
        high=n-2
        
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            
            if arr[mid]<arr[mid-1]:
                high=mid-1
            else:
                low=mid+1