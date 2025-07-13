class Solution:

   def InfixtoPostfix(self, s):
        prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
        stack, res = [], []
        for c in s:
            if c.isalnum():
                res.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and prec.get(stack[-1], 0) >= prec.get(c, 0):
                    res.append(stack.pop())
                stack.append(c)
        while stack:
            res.append(stack.pop())
        return ''.join(res)