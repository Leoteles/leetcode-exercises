# https://leetcode.com/problems/sort-colors/

#solution 17% 61%
#%%
from collections import Counter
class Solution:
    #         """
    #         Do not return anything, modify nums in-place instead.
    #         """
    def sortColors(self, nums):
        counter = Counter(nums)
        idx_num = 0
        #For red, white and blue
        for i in range(3):
            n = counter[i]
            for j in range(n):
                nums[idx_num] = i
                idx_num += 1
        # return nums
                


nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
Solution().sortColors(nums)
print(nums)

nums = [2,0,1]
# Output: [0,1,2]
Solution().sortColors(nums)
print(nums)
