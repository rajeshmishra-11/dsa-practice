from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def findpaths(self,root,paths,path):
        if root is None:
            return 
        path.append(root.data)
        if root.left is None and root.right is None:
            paths.append(list(path))
            
        self.findpaths(root.left,paths,path)
        self.findpaths(root.right,paths,path)
        
        path.pop()
        
            
        
            
    def Paths(self, root):
        if root is None:
            return 
        paths=[]
        path=[]
        self.findpaths(root,paths,path)
        return paths