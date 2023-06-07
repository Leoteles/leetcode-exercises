# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 13:47
#Solution 33% 16%
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            
            if i in '+-*/':
                a = stack.pop()
                b = stack.pop()
                #do op
                if i == '+':
                    res = a+b
                elif i == '-':
                    res = b - a
                elif i == '*':
                    res = a*b
                elif i == '/':
                    res = b/a
                stack.append(int(res))
            else:
                stack.append(int(i))
        return int(stack[0])
    
#%%
# solution 16% 16%
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while tokens:
            i = tokens.pop(0)
            if i in '+-*/':
                a = int(stack.pop())
                b = int(stack.pop())
                #do op
                if i == '+':
                    res = a+b
                elif i == '-':
                    res = b - a
                elif i == '*':
                    res = a*b
                elif i == '/':
                    res = b/a
                stack.append(res)
            else:
                stack.append(int(i))
        return int(stack[0])

