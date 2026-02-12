
from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        q=deque()
        mod=100000
        end=end%mod
        steps=[float('inf')]*mod
        steps[start%mod]=0
        q.append((0,start%mod))
        while q:
            step,val=q.popleft()
            if val==end:
                return steps[val]
            for i in arr:
                new_val=(val*i)%mod
                if steps[new_val]>step+1:
                    q.append((step+1,new_val))
                    steps[new_val]=step+1
                    
        return -1