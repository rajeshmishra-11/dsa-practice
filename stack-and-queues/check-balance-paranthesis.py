class Solution:
    def isBalanced(self, s):
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
                
            else:
                if not stack:
                    return False
                ch=stack[-1]
                stack.pop()
                
                if i==')' and ch!='(' or i==']' and ch!='[' or i=='}' and ch!='{':
                    return False
            
        return not stack