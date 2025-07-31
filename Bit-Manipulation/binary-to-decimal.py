class Solution:
	def binaryToDecimal(self, b):
		n=len(b)
		num=0
		p2=1
		for i in range(n-1,-1,-1):
		    if b[i]=='1':
		        num=num+p2
		        
		    p2=p2*2
		
		return num