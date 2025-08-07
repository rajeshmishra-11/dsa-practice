class Solution:
    
    def fun(self,n):
        if n%4==1:
            return 1
        elif n%4==2:
            return n+1
        elif n%4==3:
            return 0
        else:
            return n
        
        
    
    def findXOR(self, l, r):
        return self.fun(l-1)^self.fun(r)