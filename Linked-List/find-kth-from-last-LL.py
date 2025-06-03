class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None

#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        fast=head
        slow=head
        for i in range(k):
            if fast is None:
                return -1
            fast=fast.next
            
        while fast:
            slow=slow.next
            fast=fast.next
            
            
        return slow.data