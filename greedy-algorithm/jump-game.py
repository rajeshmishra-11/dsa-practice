class Solution:
    # Function to check if we can reach the last index from the 0th index.
    def canReach(self, arr):
        maxindex=0
        n=len(arr)
        if n==1:
            return True
        for i in range(0,n):
            if i>maxindex:
                return False
            elif maxindex>=n:
                return True
            maxindex=max(maxindex,i+arr[i])