class Solution:
    def calculateSpan(self, arr):
        n=len(arr)
        st=[]
        res=[]
        for i in range(n):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if not st:
                days=i+1
            else:
                days=i-st[-1]
            res.append(days)
            st.append(i)
        return res