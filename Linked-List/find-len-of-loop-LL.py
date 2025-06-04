'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def find_len(self,slow,fast):
        fast=fast.next
        cnt=1
        while fast!=slow:
            cnt+=1
            fast=fast.next
        return cnt
        
    def countNodesInLoop(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return self.find_len(slow,fast)
        
        return 0