# https://leetcode.com/problems/first-bad-version/
#%%
# 75% 12%
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# O(log(n)) solution using binary search
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n
        
        while left < right:
            #to avoid overflow
            # i =  left+(right-left)//2;
            i = (left + right) // 2
            #print(i)
            if isBadVersion(i):
                right = i
            else:
                left = i + 1
        return left

#%%
#solucao o(n)
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1,n+1):
            if isBadVersion(i):
                return i

#%%