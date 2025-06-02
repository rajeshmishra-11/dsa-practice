class Solution:
    # Function to insert a node at the beginning of the linked list
    def insertAtBegining(self, head, x):
        temp=Node(x)
        temp.next=head
        head=temp
        return head