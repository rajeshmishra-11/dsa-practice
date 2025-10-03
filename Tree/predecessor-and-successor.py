'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        successor=None
        predecessor=None
        temp=root
        while temp:
            if temp.data>key:
                successor=temp
                temp=temp.left
                
            else:
                temp=temp.right
                
        while root:
            if root.data<key:
                predecessor=root
                root=root.right
            
            else:
                root=root.left
                
        return predecessor, successor