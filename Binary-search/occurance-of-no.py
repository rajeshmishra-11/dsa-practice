class Solution:
        
    def countFreq(self, arr, target):
        
        n=len(arr)
        low=0
        high=n-1
        first=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                first=mid
                high=mid-1
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
                
        if first==-1:
            return 0
            
        low=0
        high=n-1
        second=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                second=mid
                low=mid+1
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
                
        return second-first+1