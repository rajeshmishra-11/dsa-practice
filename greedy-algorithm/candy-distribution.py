class Solution:
    def minCandy(self, arr):
        i=1
        total=1
        n=len(arr)
        while i<n:
            if arr[i]==arr[i-1]:
                total+=1
                i+=1
                continue
            peek=1
            while i<n and arr[i]>arr[i-1]:
                peek+=1
                total+=peek
                i+=1
            low=1
            while i<n and arr[i]<arr[i-1]:
                total+=low
                low+=1
                i+=1
            
            if low>peek:
                total+=low-peek
            
        return total