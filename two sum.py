#https://leetcode.com/problems/two-sum

#Solution 19% 33%
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,(len(nums))):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
#Solution 95% 15%
class Solution:
    def twoSum(self, nums, target):
        previous = {}
        for idx,a in enumerate(nums):
            if target - a in previous:
                #print('achei',idx,a,previous[target-a])
                return [previous[target-a],idx]
            else:
                previous[a] = idx

        return None
