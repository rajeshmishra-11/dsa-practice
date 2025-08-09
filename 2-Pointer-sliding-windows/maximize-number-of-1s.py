class Solution:
    def maxOnes(self, arr, k):
        l=0
        r=0
        n=len(arr)
        maxlen=0
        zeros=0
        while r<n:
            if arr[r]==0:
                zeros+=1
            if zeros>k:
                if arr[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen