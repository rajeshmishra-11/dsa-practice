'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def sortedMerge(self,head1, head2):
        t1=head1
        t2=head2
        dnode=Node(-1)
        temp=dnode
        while t1!=None and t2!=None:
            if t1.data<t2.data:
                temp.bottom=t1
                temp=t1
                t1=t1.bottom
            
            else:
                temp.bottom=t2
                temp=t2
                t2=t2.bottom
            
        if t1:
            temp.bottom=t1
        else:
            temp.bottom=t2
            
        return dnode.bottom
        
    def flatten(self, root):
        if root==None or root.next==None:
            return root
        merge_head=self.flatten(root.next)
        
        return self.sortedMerge(root,merge_head)