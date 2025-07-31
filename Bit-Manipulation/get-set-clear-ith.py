class Solution:
    def bitManipulation(self, num, i):
        get_ith=(num>>i-1) & 1
        set_ith=num | (1<<i-1)
        clear_ith=num & ~(1<<i-1)
        print(get_ith,set_ith,clear_ith)