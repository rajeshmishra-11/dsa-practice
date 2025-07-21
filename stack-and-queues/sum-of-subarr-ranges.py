class Solution:
    def subarrayRanges(self, arr):
        n=len(arr)
        nse=[0]*n
        pse=[0]*n
        st=[]
        #block for finding privious smallest element
        for i in range(0,n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
                
            pse[i]=st[-1] if st else -1
            st.append(i)
        st.clear()
        # block for finding next samllest element
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            nse[i]=st[-1] if st else n
            st.append(i)
            
        sumofmin=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            sumofmin+=left*right*arr[i]
            
        st.clear()
        nge=[0]*n
        pge=[0]*n
        # block for finding the next greatest element
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]<arr[i]:
                st.pop()
            nge[i]=st[-1] if st else n
            st.append(i)
            
        st.clear()
        # block for finding the privious greatest element
        for i in range(0,n):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            pge[i]=st[-1] if st else -1
            st.append(i)
        
        sumofmax=0
        # block for finding sum of subarray maximum
        for i in range(n):
            left=i-pge[i]
            right=nge[i]-i
            sumofmax+=left*right*arr[i]
        ans=sumofmax-sumofmin
        return ans