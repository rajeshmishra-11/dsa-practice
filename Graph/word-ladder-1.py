from collections import deque
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		if startWord==targetWord:
		    return 0
		
		st=set(wordList)    
		res=0
		
		m=len(startWord)
		words=deque()
		words.append(startWord)
		
		while words:
		    res+=1
		    length=len(words)
		    
		    for _ in range(length):
		        word=words.popleft()
		        
		        for j in range(m):
		            ch=word[j]
		            
		            for c in range(ord('a'),ord('z')+1):
		                word=word[:j]+chr(c)+word[j+1:]
		                
		                if word not in st:
		                    continue
		                
		                if word == targetWord:
		                    return res+1
		                    
		                st.remove(word)
		                
		                words.append(word)
		                
		            word=word[:j]+ch+word[j+1:]
		            
		            
        return 0