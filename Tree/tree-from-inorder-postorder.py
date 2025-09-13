'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''        
        

class Solution:
    def buildTree(self, in_order, post_order):
        inorder_index={val: ind for ind,val in enumerate(in_order)}
        
        self.post_index=len(post_order)-1
        
        def array_to_tree(left,right):
            if left>right:
                return None
                
            root_val=post_order[self.post_index]
            self.post_index-=1
            root=Node(root_val)
            
            if left==right:
                return root
                
            cur_index=inorder_index[root_val]
            
            root.right=array_to_tree(cur_index+1,right)
            root.left=array_to_tree(left,cur_index-1)
            
            
            return root
            
        return array_to_tree(0,len(in_order)-1)