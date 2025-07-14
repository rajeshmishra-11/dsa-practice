class Solution:
# if stand in the one element and all value in the right side from that position is less then that value then the perticular value is called as leader value
    def leaders(self, arr):
        n=len(arr)
        leader=[]
        maxm=arr[n-1]
        leader.append(arr[n-1])
        for i in range(n-2,-1,-1):
            if arr[i]>=maxm:
                leader.append(arr[i])
                maxm=arr[i]
        leader.reverse()
        return leader