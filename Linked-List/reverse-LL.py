# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        temp=head
        prev=None
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev