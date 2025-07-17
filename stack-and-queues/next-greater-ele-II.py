class Solution:
    def nextLargerElement(self, arr):
        n=len(arr)
        nge=[]
        st=[]
        for i in range(n*2-1,-1,-1):
            while st and st[-1]<=arr[i%n]:
                st.pop()
            if i<n:
                if not st:
                    nge.append(-1)
                else:
                    nge.append(st[-1])
            st.append(arr[i%n])
        return nge[::-1]