class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
        index=-1
        # Find the first decreasing element from the right
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break

        # Entire array is in descending order; just reverse to get the first permutation
        if index==-1:
            return nums.reverse()

        # Find the next greater element to swap
        for i in range(n-1,index,-1):
            if nums[i]>nums[index]:
                 nums[i],nums[index]=nums[index],nums[i]
                 break

        # Reverse the suffix
        nums[index + 1:] = reversed(nums[index + 1:])

        return nums