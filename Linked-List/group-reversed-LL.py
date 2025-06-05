"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    
    def find_kthnode(self,temp,k):
        
        while temp!=None and k>1:
            k-=1
            temp=temp.next
        return temp
    
    def reverseList(self, head):
        temp=head
        prev=None
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    
    def reverseKGroup(self, head, k):
        temp=head
        prevnode=None
        while temp!=None:
            kth_node=self.find_kthnode(temp,k)
            if kth_node==None:
                newhead=self.reverseList(temp)
                if prevnode:
                    prevnode.next=newhead
                else:
                    head=newhead
                break
            
            nextnode=kth_node.next
            kth_node.next=None
            new_head=self.reverseList(temp)
            if head==temp:
                head=new_head
            else:
                prevnode.next=new_head
                
            prevnode=temp
            temp=nextnode
        return head
    