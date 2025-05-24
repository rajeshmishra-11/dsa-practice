class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        nums.sort()
        ans=set()
        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    sumof=nums[i]
                    sumof+=nums[j]
                    sumof+=nums[k]
                    sumof+=nums[l]
                    if sumof==target:
                        temp=tuple([nums[i],nums[j],nums[k],nums[l]])
                        ans.add(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1 
                        while k<l and nums[l]==nums[l+1]:
                            l-=1 

                    elif sumof < target:
                            k+=1
                    else:
                            l-=1
        return [list(t) for t in ans]     