class Solution:
    def countSubstring(self, s):
        cnt=0
        n=len(s)
        lastseen=[-1,-1,-1]
        for i in range(0,n):
            indx=ord(s[i])-ord('a')
            lastseen[indx]=i
            cnt+=1+min(lastseen[0],lastseen[1],lastseen[2])
        return cnt