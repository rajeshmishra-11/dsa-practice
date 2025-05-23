class Solution(object):
    def maxProduct(self, nums):
        pref=1
        suffx=1
        n=len(nums)
        ans=float('-inf')
        for i in range(0,n):
            if pref==0:
                pref=1
            if suffx==0:
                suffx=1
            pref*=nums[i]
            suffx*=nums[n-i-1]
            ans=max(ans,pref,suffx)
        return ans