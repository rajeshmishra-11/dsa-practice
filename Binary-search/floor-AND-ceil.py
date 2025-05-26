class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        floor=-1
        ceil=-1
        N=len(arr)
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]<=x:
                floor=arr[mid]
                low=mid+1
            
            else:
                high=mid-1
                
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]>=x:
                ceil=arr[mid]
                high=mid-1
            
            else:
                low=mid+1
        
        
        return [floor,ceil]               