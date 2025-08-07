class Solution:
    def divide(self, dividend, divisor):
        n=abs(dividend)
        d=abs(divisor)
            
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        sign = (dividend < 0) == (divisor < 0)
        
        ans=0   
        while n>=d:
            cnt=0
            while n>=(d<<cnt):
                cnt+=1
            cnt-=1
            n-=(d<<cnt)
            ans+=(1<<cnt)
        
        return ans if sign else -ans