'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        
        temp=head
        while temp!=None and temp.next!=None:
            nextnode=temp.next
            
            while nextnode!=None and nextnode.data==temp.data:
                nextnode=nextnode.next
            temp.next=nextnode
            if nextnode!=None:
                nextnode.prev=temp
            temp=temp.next
    
        return head