class Solution:
    def checkKthBit(self, n, k):
        if 1 & n>>k==0:
            return False
        else:
            return True