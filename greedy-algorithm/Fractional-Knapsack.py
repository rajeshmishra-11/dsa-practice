class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        pairs=list(zip(val,wt))
        pairs.sort(key=lambda x:x[0]/x[1], reverse=True)
        arr1,arr2=zip(*pairs)
        n=len(arr1)
        total=0
        for i in range(0,n):
            if arr2[i]<=capacity:
                total+=arr1[i]
                capacity-=arr2[i]
            else:
                total+=(arr1[i]/arr2[i])*capacity
                break
                
        return total
    