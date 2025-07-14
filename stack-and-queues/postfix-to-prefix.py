class Solution:
    def postToPre(self, post_exp):
        n=len(post_exp)
        st=[]
        i=0
        while i<n:
            if post_exp[i].isalnum():
                st.append(post_exp[i])
            else:
                t1=st[-1]
                st.pop()
                t2=st[-1]
                st.pop()
                ans=post_exp[i]+t2+t1
                st.append(ans)
            i+=1
        return st[-1]