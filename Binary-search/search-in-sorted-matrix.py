class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        n=len(mat)
        m=len(mat[0])
        low=0
        high=(n*m)-1
        		
        while low<=high:
            mid=(low+high)//2
            # give the row index
            row=mid//m
            # give the column index
            col=mid%m
            if mat[row][col]==x:
                return True
            elif mat[row][col]<x:
                low=mid+1
            else:
                high=mid-1
                
                
        return False