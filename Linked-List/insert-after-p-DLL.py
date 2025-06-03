class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        if head==None:
            return Node(x)
        
        temp=head
        cnt=0
        while temp!=None:
            cnt+=1
            temp=temp.next
            if cnt==p:
                break
            
        front=temp.next
        
        if front==None:
            new=Node(x)
            new.prev=temp
            temp.next=new
            return head
        
        new=Node(x)
        new.next=front
        new.prev=temp
        front.prev=new
        temp.next=new
        return head