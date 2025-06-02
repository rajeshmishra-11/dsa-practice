# your task is to complete this function
# function should return new head pointer


class node:
    def __init__(self):
        self.data = None
        self.next = None


def deleteNode(head, x):
    if head==None:
        return None
    
    if x==1:
        temp=head
        head=head.next
        temp.next=None
        return head
    
    cnt=0
    temp=head
    prev=None
    while temp!=None:
        cnt+=1
        if cnt==x:
            prev.next=prev.next.next
            temp=None
            break
        prev=temp
        temp=temp.next
    return head