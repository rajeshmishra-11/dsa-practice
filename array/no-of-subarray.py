class Solution(object):
    def subarraySum(self, nums, k):
        presum=0
        dic={0:1}
        cnt=0
        for i in range(len(nums)):
            presum+=nums[i]
            more=presum-k
            cnt+=dic.get(more,0)
            dic[presum]=dic.get(presum,0)+1
        return cnt