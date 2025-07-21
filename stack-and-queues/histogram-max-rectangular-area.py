class Solution:
    def getMaxArea(self,arr):
        st=[]
        maxarea=0
        n=len(arr)
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                element=st[-1]
                st.pop()
                nse=i
                pse=-1 if not st else st[-1]
                maxarea=max(arr[element]*(nse-pse-1),maxarea)
            st.append(i)
            
        while st:
            nse=n
            element=st[-1]
            st.pop()
            pse=-1 if not st else st[-1]
            maxarea=max(arr[element]*(nse-pse-1),maxarea)
        return maxarea