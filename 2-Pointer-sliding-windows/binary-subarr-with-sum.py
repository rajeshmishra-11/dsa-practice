class Solution:
    def fun(self,arr,t):
        l=0
        r=0
        sum_=0
        cnt=0
        
        if t<0:
            return 0
            
        while r<len(arr):
            sum_+=arr[r]
            while sum_>t:
                sum_-=arr[l]
                l+=1
            cnt+=r-l+1
            r+=1
        return cnt
                
    def numberOfSubarrays(self, arr, target):
        x=self.fun(arr,target)
        y=self.fun(arr,target-1)
        return x-y