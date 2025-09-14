'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def serialize(self, root):
        arr=[]
        q=deque([root])
        while q:
            curr=q.popleft()
            
            if not curr:
                arr.append(-1)
                continue
            arr.append(curr.data)
            q.append(curr.left)
            q.append(curr.right)
            
        return arr
                
            

    def deSerialize(self, arr):
        if arr[0]==-1:
            return None
            
        root=Node(arr[0])
        q=deque([root])
        
        
        i=1
        
        while q:
            curr=q.popleft()
            if arr[i]!=-1:
                left=Node(arr[i])
                curr.left=left
                q.append(left)
                
            i+=1
            
            if arr[i]!=-1:
                right=Node(arr[i])
                curr.right=right
                q.append(right)
                
            i+=1
        return root