class Solution:
    def lowerBound(self, arr, target):
        n=len(arr)
        ans=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]>=target:
                ans=mid
                high=mid-1
            
            else:
                low=mid+1
        
        return ans
        
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
        
    def find(self, arr, x):
        n=len(arr)
        lb=self.lowerBound(arr,x)
        if lb==n or arr[lb]!=x:
            return [-1,-1]
        ub=self.upperBound(arr,x)
        return [lb,ub-1]