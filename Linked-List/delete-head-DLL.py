def deleteHead(head):
    if head==None or head.next==None:
        return None
    temp=head
    head=head.next
    head.prev=None
    temp.next=None
    return head