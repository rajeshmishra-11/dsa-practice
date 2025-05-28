
class Solution:
    def division_of_task(sself,arr,worker):
        cnt_worker=1
        work=0
        for i in range(len(arr)):
            if work+arr[i]<=worker:
                work+=arr[i]
            else:
                cnt_worker+=1
                work=arr[i]
                
        return cnt_worker
        
    def minTime (self, arr, k):
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            works=self.division_of_task(arr,mid)
            if works>k:
                low=mid+1
            else:
                high=mid-1
        return low