from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        maxlen=0
        n=len(s)
        l=0
        r=0
        maxf=0
        freq=defaultdict(int)
        while r<n:
            indx=ord(s[r])-ord('A')
            freq[indx]+=1
            maxf=max(maxf,freq[indx])
            if (r-l+1)-maxf>k:
                ind=ord(s[l])-ord('A')
                if freq[ind]!=0:
                    freq[ind]-=1
                l+=1
            if (r-l+1)-maxf<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
                