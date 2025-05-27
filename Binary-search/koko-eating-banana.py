class Solution:
    def total_hour(self,arr,hour):
        time_taken=0
        for i in range(0,len(arr)):
            time_taken+=(arr[i]+hour-1)//hour
            
        return time_taken

    #how many minimum bananas they want to eat in one hour to eat all the banana in a k times or less then the time limit
    
    def kokoEat(self,arr,k):
        high=max(arr)
        low=1
        while low <=high:
            mid=(low+high)//2
            total_time_taken=self.total_hour(arr,mid)
            if total_time_taken<=k:
                high=mid-1
            else:
                low=mid+1
        return low