# https://leetcode.com/problems/contains-duplicate/

# solution 21% 40%
from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(Counter(nums)) != len(nums)


nums = [1,2,3,1]


#%%
# solution 46% 24%
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        

#%%

# solution 37% 14%
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set()
        for i in nums:
            if i in my_set:
                return True
            else:
                my_set.add(i)
            

#%%
# solution 33% 40%
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter_dict = {}
        for i in nums:
            if i in counter_dict:
                return True
            else:
                counter_dict[i] = 1
        return False

nums = [1,2,3,1]
Solution().containsDuplicate(nums)



