# https://leetcode.com/problems/search-in-rotated-sorted-array/
#%%

# Solution 43% 55%
class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left_i,right_i = 0,len(nums)-1
        while left_i < right_i:
            middle_i = (right_i + left_i)//2
            if nums[middle_i] == target:
                return middle_i
            elif nums[left_i] == target:
                return left_i
            elif nums[right_i] == target:
                return right_i
            # first half is ascending
            if nums[left_i] < nums[middle_i]: 
                if nums[left_i] < target < nums[middle_i]:
                    right_i = middle_i - 1
                else:
                    left_i = middle_i + 1
            # second half is ascending
            else:
                if nums[middle_i] < target < nums[right_i]:
                    left_i = middle_i + 1
                else:
                    right_i = middle_i - 1
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
#Expected 4
print(Solution().search(nums,target))

# nums = [4,5,6,7,0,1,2]
# target = 0
# #Output: 4
# print(Solution().search(nums,target))

# nums = [4,5,6,7,0,1,2]
# target = 3
# #Output: -1
# print(Solution().search(nums,target))

# nums = [1]
# target = 0
# #Output: -1
# print(Solution().search(nums,target))


# nums = [1,3]
# target = 2
# print(Solution().search(nums,target))
#Output: -1
