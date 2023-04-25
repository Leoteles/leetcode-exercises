# https://leetcode.com/problems/binary-search/
#29% 31%
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.get_index(nums,target)

    def get_index(self,nums,target,left_index = None,right_index = None):

        if left_index is None or right_index is None:
            left_index = 0
            right_index  = len(nums)

        if not len(nums[left_index:right_index]):
            return -1

        i = left_index + len(nums[left_index:right_index])//2

        if target > nums[i]:
            left_index  = i + 1
            idx = self.get_index(nums,target,left_index,right_index)
        elif target < nums[i]:
            right_index  = i
            idx = self.get_index(nums,target,left_index,right_index)
        else:
            idx = i
        return idx