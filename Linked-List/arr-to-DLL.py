class Node:
	def __init__(self, data):   # data -> value stored in node
	    self.data = data
	    self.next = None
	    self.prev = None

class Solution:
    def constructDLL(self, arr):
        
        if not arr:
            return None
            
        head=Node(arr[0])
        cur=head
        
        for i in range(1,len(arr)):
            new=Node(arr[i])
            new.prev=cur
            cur.next=new
            cur=new
        return head