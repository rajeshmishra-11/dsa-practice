from collections import defaultdict
class Solution:
    def smallestWindow(self, s1, s2):
        
        freq=defaultdict(int)
        n=len(s1)
        m=len(s2)
        if n<m:
            return ""
        for i in  range(0,m):
            indx=ord(s2[i])
            freq[indx]+=1
        l=0
        r=0
        cnt=0
        sindex=-1
        minlen=float('inf')
        window=defaultdict(int)
        while r<n:
            index=ord(s1[r])
            window[index]+=1
            if freq[index] > 0 and window[index] <= freq[index]:
                cnt += 1
            
            while cnt==m:
                if r-l+1<minlen:
                    minlen=r-l+1
                    sindex=l
                    
                left_index=ord(s1[l])
                window[left_index]-=1
                if freq[left_index] > 0 and window[left_index] < freq[left_index]:
                    cnt-=1
                l+=1
            r+=1
        return "" if sindex == -1 else s1[sindex:sindex + minlen]
                    
                