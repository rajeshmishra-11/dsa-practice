# Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def searchKey(self, n, head, key):
        cur=head
        while cur is not None:
            if cur.data==key:
                return True
            cur=cur.next
        return False