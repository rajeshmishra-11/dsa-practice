class Solution(object):
    def twoSum(self, nums, target):
        hmap={}
        n=len(nums)
        for i in range(0,n):
            more=target-nums[i]

            if more in hmap:
                ans=[hmap[more],i]
            hmap[nums[i]]=i
        return ans