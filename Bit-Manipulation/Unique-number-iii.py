class Solution:
    def getSingle(self, arr):
        n=len(arr)
        arr.sort()
        i=0
        while i<n-1:
            if arr[i]==arr[i+1]:
                i+=3
            else:
                return arr[i]
        return arr[n-1]