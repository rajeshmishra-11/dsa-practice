  
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Solution:
    def insertAtEnd(self, head, x):
        if head==None:
            return Node(x)
        temp=head
        while temp.next!=None:
            temp=temp.next
            
        newnode=Node(x)
        temp.next=newnode
        return head