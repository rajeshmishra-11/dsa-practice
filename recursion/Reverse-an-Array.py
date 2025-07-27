class Solution:
    def fun(self,l,r,arr):
        if l>=r:
            return
        arr[l],arr[r]=arr[r],arr[l]
        self.fun(l+1,r-1,arr)
        
    def reverseArray(self, arr):
        n=len(arr)
        self.fun(0,n-1,arr)
        return arr