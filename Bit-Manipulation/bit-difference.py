class Solution:
    def countBitsFlip(self, a, b):
        ans=a^b
        cnt=0
        for i in range(0,31):
            if ans&(1<<i):
                cnt+=1
        
        return cnt