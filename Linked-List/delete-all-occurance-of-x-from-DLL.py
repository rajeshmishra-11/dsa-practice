'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        temp=head
        while temp!=None:
            if temp.data==x:
                if temp==head:
                    head=head.next
                    
                prevnode=temp.prev
                nextnode=temp.next
                
                if temp.next!=None:
                    nextnode.prev=prevnode
                if temp.prev!=None:
                    prevnode.next=nextnode
                
                temp=nextnode
            else:
                temp=temp.next
                
        return head