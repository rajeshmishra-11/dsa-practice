'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    
    def sortedMerge(self,head1, head2):
        t1=head1
        t2=head2
        dnode=Node(-1)
        temp=dnode
        while t1!=None and t2!=None:
            if t1.data<t2.data:
                temp.next=t1
                temp=t1
                t1=t1.next
            
            else:
                temp.next=t2
                temp=t2
                t2=t2.next
            
        if t1:
            temp.next=t1
        else:
            temp.next=t2
            
        return dnode.next
    
    def find_mid(self,head):
        fast=head.next
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow
    
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if head==None or head.next==None:
            return head
        temp=head
        mid=self.find_mid(head)
        left=temp
        right=mid.next
        mid.next=None
        
        left_head=self.mergeSort(left)
        right_head=self.mergeSort(right)
        
        return self.sortedMerge(left_head,right_head)
        