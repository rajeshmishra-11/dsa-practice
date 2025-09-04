'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def fun(self,root,level,arr):
        if root is None:
            return arr
        if level==len(arr):
            arr.append(root.data)
        self.fun(root.left,level+1,arr)
        self.fun(root.right,level+1,arr)
        if len(arr)==0:
            return []
        else:
            return arr
    
    def LeftView(self, root):
        arr=[]
        return self.fun(root,0,arr)