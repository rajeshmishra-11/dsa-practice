class Solution:
    def medianOf2(self, a, b):
        n1=len(a)
        n2=len(b)
        n=n1+n2
        ind2=n//2
        ind1=ind2-1
        ind1el=-1
        ind2el=-1
        i=0
        j=0
        cnt=0
        while i < n1 and j < n2:
            if a[i] <= b[j]:
                if cnt == ind1:
                    ind1el = a[i]
                if cnt == ind2:
                    ind2el = a[i]
                i += 1
            else:
                if cnt == ind1:
                    ind1el = b[j]
                if cnt == ind2:
                    ind2el = b[j]
                j += 1
            cnt += 1
                
        while i<n1:
            if cnt==ind1:
                ind1el=a[i]
            if cnt==ind2:
                ind2el=a[i]
                    
            i+=1
            cnt+=1
            
        while j<n2:
            if cnt==ind1:
                ind1el=b[j]
            if cnt==ind2:
                ind2el=b[j]
                    
            j+=1
            cnt+=1
            
        
        if n % 2 == 1:
            return float(ind2el)
        else:
            return round((ind1el + ind2el) / 2.0, 2)