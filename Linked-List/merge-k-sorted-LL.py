'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:

    
    def mergeKLists(self, arr):
        heap=[]
        
        for node in arr:
            if node:
                heapq.heappush(heap,node)
                
        dnode=Node(-1)
        temp=dnode
        
        while heap:
            min_heap=heapq.heappop(heap)
            temp.next=min_heap
            temp=min_heap
            
            if min_heap.next:
                heapq.heappush(heap,min_heap.next)
            
        return dnode.next