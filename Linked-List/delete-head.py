class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteHead(head):
    if head==None:
        return None
    temp=head
    head=head.next
    temp.next=None
    return head