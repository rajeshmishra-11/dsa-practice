class Solution:
    def postToInfix(self, s):
        n=len(postfix)
        st=[]
        i=0
        
        while i<n:
            if s[i].isalnum():
                st.append(s[i])
                
            else:
                t1=st[-1]
                st.pop()
                t2=st[-1]
                st.pop()
                ans='('+t2+s[i]+t1+')'
                st.append(ans)
                
            i+=1
            
        return st[-1]