class Solution:
    def longestUniqueSubstring(self, s):
        l=0
        r=0
        maxlen=0
        hash_tab=[-1]*256
        n=len(s)
        while r<n:
            char_indx=ord(s[r])
            if hash_tab[char_indx]!=-1:
                if hash_tab[char_indx]>=l:
                    l=hash_tab[char_indx]+1
            lenth=r-l+1
            maxlen=max(lenth,maxlen)
            hash_tab[char_indx]=r
            r+=1
        return maxlen