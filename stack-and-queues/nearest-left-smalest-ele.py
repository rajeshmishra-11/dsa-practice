class Solution:
    def leftSmaller(self, arr):
        n=len(arr)
        st=[]
        nse=[]
        for i in range(n):
            while st and st[-1]>=arr[i]:
                st.pop()
            if not st:
                nse.append(-1)
            else:
                nse.append(st[-1])
            st.append(arr[i])
        return nse