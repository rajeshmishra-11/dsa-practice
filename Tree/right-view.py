'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def fun(self,root,level,arr):
        if root is None:
            return 
        if level==len(arr):
            arr.append(root.data)
        self.fun(root.right,level+1,arr)
        self.fun(root.left,level+1,arr)
        return arr
        
    def rightView(self,root):
        arr=[]
        self.fun(root,0,arr)
        return arr