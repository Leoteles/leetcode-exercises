# https://leetcode.com/problems/valid-parentheses/
# 61% 13%

#from collections import deque
class Solution(object):
    
    closings = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = []#deque()
        for i in s:
            # print(i)
            #openings
            if i not in self.closings:
                #Not of closings type, so opening type, insert
                d.append(i)
            #closings
            else:
                #No opening for this closing
                if not len(d):
                    return False
                #If opening for this  closing, pop the opening
                if  d[-1] == self.closings[i]:
                    #Found a match
                    d.pop()
                else:
                    return False
        return len(d)==0


# s = "()"
# s = "()[]{}"
# s = "(]"
# Solution().isValid(s)
