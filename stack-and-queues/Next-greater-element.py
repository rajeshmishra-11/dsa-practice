class Solution:
    def nextLargerElement(self, arr):
        n=len(arr)
        nge=[]
        st=[]
        for i in range(n-1,-1,-1):
            while st and st[-1]<=arr[i]:
                st.pop()
            if not st:
                nge.append(-1)
            else:
                nge.append(st[-1])
            
            st.append(arr[i])
        return reversed(nge)