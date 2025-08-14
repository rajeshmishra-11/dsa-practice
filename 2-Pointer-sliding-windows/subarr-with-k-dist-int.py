from collections import defaultdict
class Solution:
    def fun(self,arr,k):
        if k<0:
            return 0
        n=len(arr)
        l=0
        r=0
        subarray=0
        freq=defaultdict(int)
        
        while r<n:
            freq[arr[r]]+=1
            while len(freq)>k:
                freq[arr[l]]-=1
                if freq[arr[l]]==0:
                    del freq[arr[l]]
                l+=1
            if len(freq)<=k:
                subarray+=r-l+1
            r+=1
        return subarray
    def exactlyK(self, arr, k):
        return self.fun(arr,k)-self.fun(arr,k-1)