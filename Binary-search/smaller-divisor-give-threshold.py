class Solution:
    def sumof(self,arr,d):
        sum_of=0
        for i in range(len(arr)):
            # this will return the next rount of value like 2.3->3 etc
            sum_of+=(arr[i]+d-1)//d
        return sum_of
            
    def smallestDivisor(self, arr, k):
        low=1
        high=max(arr)
        ans=-1
        
        if k<len(arr):
            return -1
            
        while low<=high:
            mid=(low+high)//2
            if self.sumof(arr,mid)<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
                
        return ans