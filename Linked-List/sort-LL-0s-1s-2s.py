# Node Class
class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
	
class Solution:
    def segregate(self, head):
        zerohead=Node(-1)
        onehead=Node(-1)
        twohead=Node(-1)
        zero=zerohead
        one=onehead
        two=twohead
        temp=head
        
        
        while temp!=None:
            if temp.data==0:
                zero.next=temp
                zero=temp
            elif temp.data==1:
                one.next=temp
                one=temp
            else:
                two.next=temp
                two=temp
            temp=temp.next
            
        zero.next = onehead.next if onehead.next else twohead.next
        one.next = twohead.next
            
        two.next=None
                
        return zerohead.next