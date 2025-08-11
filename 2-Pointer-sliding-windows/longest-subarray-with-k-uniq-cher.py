from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        maxlen=-1
        l=0
        r=0
        n=len(s)
        freq=defaultdict(int)
        while r<n:
            freq[s[r]]+=1
            if len(freq)>k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            if len(freq)==k:
                maxlen=max(maxlen,r-l+1)
            r+=1
            
        return maxlen