#Function to check whether the list is palindrome.
class Solution:
    
    # function to reverse a array
    def reverse(self,head):
        temp=head
        prev=None
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            newHead=prev
        return newHead
    
    def isPalindrome(self, head):
        if head==None or head.next==None:
            return True
            
        fast=head
        slow=head
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            
        newHead=self.reverse(slow.next)
        first=head
        second=newHead
        
        while second!=None:
            if first.data!=second.data:
                self.reverse(newHead)
                return False
                
            first=first.next
            second=second.next
            
        self.reverse(newHead)
        return True