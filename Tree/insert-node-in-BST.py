'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def search(self,root,key):
        if root is None or root.data==key:
            return root
            
        if root.data<key:
            return self.search(root.right,key)
            
        elif root.data>key:
            return self.search(root.left,key)
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if self.search(root,key):
            return root
            
        parents=None
        cur=root
        while cur:
            parents=cur
            
            if cur.data<key:
                cur=cur.right
                    
            elif cur.data>key:
                cur=cur.left
                    
        node=Node(key)
        if parents.data>key:
            parents.left=node
        else:
            parents.right=node
        return root