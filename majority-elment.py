class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        ele=0
        cnt=0
# using more majority voting algorithm
        for i in range(0,n):
            if cnt==0:
                ele=nums[i]
                cnt=1
            else:
                if ele==nums[i]:
                    cnt+=1
                
                else:
                    cnt-=1
        cnt=0
        for i in range(0,n):
            if ele==nums[i]:
                cnt+=1
        if cnt>n//2:
            return ele
        return -1