'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        if head==None or head.next==None:
            return None
            
        fast=head
        slow=head
        fast=fast.next.next
        
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        slow.next=slow.next.next
        
        return head