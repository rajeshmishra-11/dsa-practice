class Solution:
    def solve(self, bt):
        wt=0
        ct=0
        n=len(bt)
        bt.sort()
        for i in range(0,n):
            wt+=ct
            ct+=bt[i]
        return wt//n