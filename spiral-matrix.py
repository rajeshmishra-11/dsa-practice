class Solution(object):
    def spiralOrder(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        left=0
        right=col-1
        top=0
        down=row-1
        ans=[]
        while left<=right and top<=down:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top,down+1):
                ans.append(matrix[i][right])
            right-=1
            if top<=down:
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                down-=1
            if left<=right:
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1

        return ans