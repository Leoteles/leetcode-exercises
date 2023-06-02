#%%
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#%%
# Solution 77% 38%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        start_idx = 0
        max_size = 0
        for i,c in enumerate(s):
            if c in last_index:
                if last_index[c] >= start_idx:
                    start_idx = last_index[c]+1
            max_size = max(max_size,i + 1 - start_idx)
            last_index[c] = i
        return max_size