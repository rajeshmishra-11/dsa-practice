class Solution:
    
    def merge(self,arr,left,mid,high):
        n1=mid-left+1
        n2=high-mid
        
        l=arr[left:mid+1]
        r=arr[mid+1:high+1]
        
        i=0
        j=0
        k=left
        while i<n1 and j<n2:
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        
        while i<n1:
            arr[k]=l[i]
            i+=1
            k+=1
            
        while j<n2:
            arr[k]=r[j]
            j+=1
            k+=1
            
    def count_pair(self,arr,low,mid,high):
        right=mid+1
        cnt=0
        for i in range(low,mid+1):
            while right<=high and arr[i]>2*arr[right]:
                right+=1
            cnt+=right-(mid+1)
                
        return cnt
            
            
    
    def merge_sort(self,arr,l,r):
        cnt=0
        if l<r:
            m=(l+r)//2
            cnt+=self.merge_sort(arr,l,m)
            cnt+=self.merge_sort(arr,m+1,r)
            cnt+=self.count_pair(arr,l,m,r)
            self.merge(arr,l,m,r)
            
        return cnt
    
    def countRevPairs(self, N, arr):
        return self.merge_sort(arr,0,N-1)