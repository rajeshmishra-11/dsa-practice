class Solution:
    def binarysearch(self, arr, k):
        n=len(arr)
        low=0
        high=n-1
        result=-1
        # elemenate the exta space
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==k:
                result=mid
                high=mid-1
            
            elif arr[mid]<k:
                low=mid+1
            
            else:
                high=mid-1
            
        return result