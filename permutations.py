#https://leetcode.com/problems/permutations/
#%%
#9:00 9:31

# DFS Solution 43% 26%
class Solution:
    def dfs(self,nums):
        if len(nums) == 1:
            return [nums]
        out = []
        for i in range(len(nums)):
            num = nums[i]
            # perms = self.dfs(nums[i+1:])
            perms = self.dfs(nums[:i]+nums[i+1:])
            perms = [[num] + perm for perm in perms]
            out.extend(perms)
        return out

    def permute(self,nums):
        out = []
        if nums is None:
            return
        elif len(nums) == 0:
            return []
        return self.dfs(nums)
        


nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute(nums))
# %%
