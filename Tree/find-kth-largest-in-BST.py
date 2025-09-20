# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        curr=root
        cnt=0
        st=[]
        
        while st or curr is not None:
            
            while curr is not None:
                st.append(curr)
                curr=curr.right
                
            curr=st.pop()
            
            cnt+=1
            
            if cnt==k:
                return curr.data
                
            curr=curr.left
            
        return -1