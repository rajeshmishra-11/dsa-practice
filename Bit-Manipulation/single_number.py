def getSingle(self,arr):
        n=len(arr)
        xor=0
        for i in range(n):
            xor=xor^arr[i]
        return xor