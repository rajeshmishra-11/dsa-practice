class Solution:
             
    def sumSubMins(self, arr):
        n=len(arr)
        nse=[0]*n
        pse=[0]*n
        st=[]
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
                
            pse[i]=st[-1] if st else -1
            st.append(i)
            
        st.clear()
        
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            nse[i]=st[-1] if st else n
            st.append(i)
            
        total=0
       
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            total+=left*right*arr[i]
        return total
        