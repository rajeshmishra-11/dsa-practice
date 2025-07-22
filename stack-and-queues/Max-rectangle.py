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
    
    def maxArea(self, mat):
        if not mat:
            return 0
        n=len(mat)
        m=len(mat[0])
        hist=[0]*m
        maxarea=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    hist[j]=0
                else:
                    hist[j]+=1
                
            maxarea=max(maxarea,self.getMaxArea(hist))
            
        return maxarea