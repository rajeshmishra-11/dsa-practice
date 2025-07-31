class Solution:
    def decToBinary(self, n):
        res=""
        if n==0:
            return 0
        while n>0:
            if n%2==1:
                res+='1'
            else:
                res+='0'
                
            n//=2
        res=res[::-1]
        return res