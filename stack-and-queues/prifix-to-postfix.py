class Solution:
    def preToPost(self,s):
        n=len(s)
        st=[]
        i=n-1
        while i>=0:
            if s[i].isalnum():
                st.append(s[i])
            else:
                t1=st[-1]
                st.pop()
                t2=st[-1]
                st.pop()
                ans=t1+t2+s[i]
                st.append(ans)
            i-=1
            
        return st[-1] if st else ""