class Solution:
    # finction to find the how many student get books
    # arr contains the no of pages in the book
    def cntstd(self,arr,pages):
        std=1
        pagesStd=0
        for i in range(len(arr)):
            if pagesStd+arr[i]<=pages:
                pagesStd+=arr[i]
                
            else:
                std+=1
                pagesStd=arr[i]
                
        return std
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        if k>len(arr):
            return -1
            
        low=max(arr)
        high=sum(arr)
        
        while low<=high:
            mid=(low+high)//2
            NoOfstd=self.cntstd(arr,mid)
            if NoOfstd>k:
                low=mid+1
            else:
                high=mid-1
                
        return low