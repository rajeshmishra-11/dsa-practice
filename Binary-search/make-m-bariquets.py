
class Solution:
    # function to check the day is possible or not for bariquets
    def possible(self,arr,days,m,k):
        cnt=0
        NoOfB=0
        for i in range(0,len(arr)):
            if arr[i]<=days:
                cnt+=1
                
            else:
                NoOfB+=cnt//k
                cnt=0
        NoOfB+=cnt//k
        if NoOfB>=m:
            return True
        else:
            return False
            
            
    def minDaysBloom(self, m, k, arr):
        n=len(arr)
        if n<m*k:
            return -1
            
        low=min(arr)
        high=max(arr)
        ans=high
            
        while low<=high:
            mid=(low+high)//2
            eligible=self.possible(arr,mid,m,k)
            if eligible==True:
                ans=mid
                high=mid-1
                        
            else:
                low=mid+1
        return ans