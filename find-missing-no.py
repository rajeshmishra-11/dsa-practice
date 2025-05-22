class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=n*(n+1)//2
        s1=sum(nums)
        res=s-s1
        return res