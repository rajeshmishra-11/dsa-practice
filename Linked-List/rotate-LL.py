'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        tail=head
        lenth=1
        while tail.next!=None:
            lenth+=1
            tail=tail.next
        
        k=k%lenth
        if k==0:
            return head
        temp=head
        while temp!=None and k>1:
            k-=1
            temp=temp.next
        tail.next=head
        head=temp.next
        temp.next=None
        return head