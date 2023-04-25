# https://leetcode.com/problems/implement-queue-using-stacks/

# 81% 40%
from collections import deque
class MyQueue(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        temp = deque()

        for i in range(len(self.stack)):
            temp.append(self.stack.pop())

        temp.append(x)
        # print(temp,self.stack)

        for i in range(len(temp)):
            # print('append to deck:',temp[-1])
            self.stack.append(temp.pop())
        # print(temp,self.stack)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0

myqueue = MyQueue()

print(myqueue.push(1),myqueue.push(2),myqueue.peek(),myqueue.pop(),myqueue.empty())
print(myqueue.stack)


#%%