class Solution(object):
    def generate(self, numRows):
        
        ans = []

        for row in range(numRows):
            temp = []
            res = 1
            for col in range(row + 1):
                if col == 0:
                    res = 1
                else:
                    res = res * (row - col + 1) // col
                temp.append(res)
            ans.append(temp)

        return ans