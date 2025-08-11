from collections import defaultdict

class Solution:
    def totalElements(self, arr):
        l=0
        r=0
        maxlen=0
        freq=defaultdict(int)
        n=len(arr)
        while r<n:
            freq[arr[r]]+=1
            if len(freq)>2:
                freq[arr[l]]-=1
                if freq[arr[l]]==0:
                    del freq[arr[l]]
                l+=1
            if len(freq)<=2:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen