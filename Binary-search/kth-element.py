class Solution:

    def kthElement(self, a, b, k):
        
        n1=len(a)
        n2=len(b)
        n=n1+n2
        kthel=-1
        i=0
        j=0
        cnt=1
        while i < n1 and j < n2:
            if a[i] <= b[j]:
                if cnt == k:
                    kthel = a[i]
                i += 1
            else:
                if cnt == k:
                    kthel = b[j]
                j += 1
            cnt += 1
                
        while i<n1:
            if cnt==k:
                kthel=a[i]
                    
            i+=1
            cnt+=1
            
        while j<n2:
            if cnt==k:
                kthel=b[j]
                    
            j+=1
            cnt+=1
            
        return kthel