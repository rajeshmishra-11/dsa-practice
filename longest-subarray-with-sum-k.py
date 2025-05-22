class Solution:
    def longestSubarray(self, arr, k):
        presumMap={}
        length=0
        prefsum=0
# The main idea is to check in the hash map x-k is avilable or not
        for i in range(len(arr)):
            prefsum+=arr[i]
            
            if prefsum==k:
                length=i+1
                
            elif prefsum-k in presumMap:
                length=max(length,i-presumMap[prefsum-k])
            
            if prefsum not in presumMap:
                presumMap[prefsum]=i
                
        return length