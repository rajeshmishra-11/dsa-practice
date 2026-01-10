from collections import deque
class Solution:
    def findOrder(self, words):
        
        graph=[[] for _ in range(26)]
        
        indegree=[0]*26
        
        exist=[False]*26
        
        for word in words:
            for ch in word:
                exist[ord(ch)-ord('a')]=True
                
                
        for i in range(len(words)-1):
            
            w1=words[i]
            w2=words[i+1]
            minlen=min(len(w1),len(w2))
            
            j=0
            while j<minlen and w1[j]==w2[j]:
                j+=1
                
            if j<minlen:
                u=ord(w1[j])-ord('a')
                v=ord(w2[j])-ord('a')
                graph[u].append(v)
                indegree[v]+=1
                
            elif len(w1)>len(w2):
                return ""
                
        
        q=deque()
        for i in range(26):
            if exist[i] and indegree[i]==0:
                q.append(i)
                
        res=[]
        
        while q:
            u=q.popleft()
            res.append(chr(u+ord('a')))
            for v in graph[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
                    
        if len(res)!=sum(exist):
            return ""
            
        return ''.join(res)