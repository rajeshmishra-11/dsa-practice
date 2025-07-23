class Solution:
    def maxOfSubarrays(self, arr, k):
        ans=[]
        dq=deque([])
        n=len(arr)
        for i in range(n):
            if dq and dq[0]<=i-k:
                dq.popleft()
                
            while dq and arr[dq[-1]]<=arr[i]:
                dq.pop()
                
            dq.append(i)
            
            if i>=k-1:
                ans.append(arr[dq[0]])
        return ans