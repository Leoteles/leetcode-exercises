#https://leetcode.com/problems/min-stack/
#%%

#Solution 20% 70%

from collections import deque
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.min_stack = deque()
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.stack)==1:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x,self.min_stack[-1]))



    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# min_stack = MinStack()
# min_stack.push(-2)
# min_stack.push(0)
# min_stack.push(-3)
# min_stack.getMin()
# min_stack.pop()
# min_stack.top()
# min_stack.getMin()
####
min_stack = MinStack()
print(min_stack.push(-2))
print(min_stack.push(0))
print(min_stack.push(-1))
print(min_stack.getMin())#-2
print(min_stack.top())#-1
print(min_stack.pop())
print(min_stack.getMin())#-2

# %%
