
class Solution:
    
    def fun(self,n):
        if n<=1:
            return n
        last=self.fun(n-1)
        slast=self.fun(n-2)
        return last + slast
    
    def nthFibonacci(self, n: int) -> int:
        return self.fun(n)
    