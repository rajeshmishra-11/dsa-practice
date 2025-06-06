# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        temp=head
        while temp!=None:
            copynode=Node(temp.data)
            copynode.next=temp.next
            temp.next=copynode
            temp=temp.next.next
            
        temp=head
        while temp!=None:
            copynode=temp.next
            if temp.random:
                copynode.random=temp.random.next
                
            else:
                copynode.random=None
                
            temp=temp.next.next
            
        dnode=Node(-1)
        temp=head
        res=dnode
        while temp!=None:
            res.next=temp.next
            temp.next=temp.next.next
            res=res.next
            temp=temp.next
            
        return dnode.next