class Solution:
    def lemonadeChange(self, N, bills):
        five=0
        ten=0
        twenty=0
        for i in range(0,N):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five:
                    ten+=1
                    five-=1
                else:
                    return False
            else:
                if five and ten:
                    twenty+=1
                    five-=1
                    ten-=1
                elif five>=3:
                    twenty+=1
                    five-=3
                else:
                    return False
        return True