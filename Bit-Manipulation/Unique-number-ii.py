class Solution:
	def singleNum(self, arr):
		xorr=0
		for i in arr:
		    xorr=xorr^i
		    
		rightmost=xorr&(xorr-1)^xorr
		
		b1=0
		b2=0
		
		for i in arr:
		    if rightmost&i:
		        b1=b1^i
		    else:
		        b2=b2^i
		if b1<b2:
		    return [b1,b2]
		else:
		    return [b2,b1]