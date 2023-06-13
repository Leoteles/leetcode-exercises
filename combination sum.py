#https://leetcode.com/problems/combination-sum/
#Solution 94% 63%
#%%
class Solution:
    out = None
    def dfs(self,candidates,target,array = None,last_idx=0):
        if array is None:
            array = []
        # for cand in candidates:
        for i in range(last_idx,len(candidates)):
            cand = candidates[i]
            if target - cand == 0:
               self.out.append(array+[cand])
            elif target - cand < 0:
                return
            else:
                self.dfs(candidates,target-cand,array.copy()+[cand],i)
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        self.out = []
        self.dfs(candidates,target)
        return self.out
candidates = [2,3,6,7]
target = 7
#Output: [[2,2,3],[7]]
print(Solution().combinationSum(candidates,target))
# %%

