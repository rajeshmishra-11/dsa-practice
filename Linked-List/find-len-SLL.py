#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        cnt=0
        cur=head
        while cur is not None:
            cnt+=1
            cur=cur.next
            
        return cnt
            