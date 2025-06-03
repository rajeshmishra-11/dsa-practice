
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head):
        last=None
        cur=head
        while cur!=None:
            last=cur.prev
            cur.prev=cur.next
            cur.next=last
            cur=cur.prev
            
        if last is not None:
            head=last.prev
        
        return head