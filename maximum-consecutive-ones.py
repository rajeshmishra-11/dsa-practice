class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        cnt=0
        maxm=0
        for i in range(0,n):
            if nums[i]==1:
                cnt+=1
                maxm=max(maxm,cnt)
            else:
                cnt=0

        return maxm