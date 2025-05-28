class Solution:
    
    def canweplace(self,arr,dist,cows):
        cntcows=1
        last=arr[0]
        n=len(arr)
        for i in range(1,n):
            if arr[i]-last>=dist:
                cntcows+=1
                last=arr[i]
                
                if cntcows>=cows:
                    return True
        return False
                
            

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n=len(stalls)
        low=1
        high=stalls[n-1]-stalls[0]
        while low<=high:
            mid=(low+high)//2
            if self.canweplace(stalls,mid,k)==True:
                low=mid+1
            else:
                high=mid-1
                
        return high