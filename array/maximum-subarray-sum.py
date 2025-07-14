class Solution(object):
    def maxSubArray(self, nums):
        maxm=nums[0]
        sumof=0
        n=len(nums)
        for i in range(0,n):
            sumof+=nums[i]
            maxm=max(maxm,sumof)
            if sumof<0:
                sumof=0
        return maxm      