class Solution:
    def removeKdigits(self, s, k):
        n=len(s)
        st=[]
        for i in range(n):
            while st and k>0 and st[-1]>s[i]:
                st.pop()
                k-=1
            st.append(s[i])
            
        while k>0:
            st.pop()
            k-=1
        if not st:
            return '0'
        res=""
        res="".join(st).lstrip('0')
        return res if res else '0'