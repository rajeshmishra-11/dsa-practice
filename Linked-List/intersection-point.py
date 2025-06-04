'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        t1=head1
        t2=head2
        while t1!=t2:
            t1=t1.next
            t2=t2.next
            
            if t1==t2:
                return t1
            
            if t1==None:
                t1=head2
            if t2==None:
                t2=head1
        
        return t1