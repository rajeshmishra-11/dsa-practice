class Solution:
    def maxChildren(self, greed, cookie):
        greed.sort()
        cookie.sort()
        l=0
        r=0
        n1=len(greed)
        n2=len(cookie)
        while l<n1 and r<n2:
            if greed[l]<=cookie[r]:
                l+=1
            r+=1
            
        return l