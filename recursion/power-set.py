class Solution:
    
    def subseq(self,ind,arr,s,res):
        n=len(s)
        if ind==n:
            if arr:
                res.append(''.join(arr))
            return
        arr.append(s[ind])
        self.subseq(ind+1,arr,s,res)
        arr.pop()
        self.subseq(ind+1,arr,s,res)
        
        
	def AllPossibleStrings(self, s):
	    res=[]
		self.subseq(0,[],s,res)
		res.sort()
		return res