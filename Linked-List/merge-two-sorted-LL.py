'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        t1=head1
        t2=head2
        dnode=Node(-1)
        temp=dnode
        while t1!=None and t2!=None:
            if t1.data<t2.data:
                temp.next=t1
                temp=t1
                t1=t1.next
            
            else:
                temp.next=t2
                temp=t2
                t2=t2.next
            
        if t1:
            temp.next=t1
        else:
            temp.next=t2
            
        return dnode.next