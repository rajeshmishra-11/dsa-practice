class Solution:
    def fun(self,arr,k):
        if k<0:
            return 0
        n=len(arr)
        l=0
        r=0
        sum_=0
        subarray=0
        while r<n:
            sum_+=((arr[r])%2)
            while sum_>k:
                sum_-=((arr[l])%2)
                l+=1
            if sum_<=k:
                subarray+=r-l+1
            r+=1
        return subarray
    def countSubarrays(self, arr, k):
        x=self.fun(arr,k)
        y=self.fun(arr,k-1)
        return x-y