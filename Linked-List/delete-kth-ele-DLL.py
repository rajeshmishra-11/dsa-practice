class Solution:
    def delete_node(self, head, x):
        if head==None or head.next==None:
            return None
        
        if x == 1:
            temp = head
            head = head.next
            if head:
                head.prev = None
            temp.next = None
            return head
            
            
        cnt=0
        temp=head
        while temp.next!=None:
            cnt+=1
            if cnt==x:
                break
            temp=temp.next
            
        back=temp.prev
        front=temp.next
        
        if back==None and front==None:
            return None
            
        elif back==None:
            temp=head
            head=head.next
            head.prev=None
            temp.next=None
            return head
            
        elif front == None:
            back.next = None
            temp.prev = None
            return head
            
        back.next=front
        front.prev=back
        temp.prev=None
        temp.next=None
        return head