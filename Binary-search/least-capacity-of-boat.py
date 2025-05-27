class Solution:
    def days(self,wt,capacity):
        day=1
        load=0
        for i in range(len(wt)):
            if load+wt[i]>capacity:
                day+=1
                load=wt[i]
            else:
                load+=wt[i]
        return day
        
    def leastWeightCapacity(self, arr, n, d):
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            no_of_days=self.days(arr,mid)
            if no_of_days<=d:
                high=mid-1
            else:
                low=mid+1
        return low