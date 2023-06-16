# https://leetcode.com/problems/merge-intervals/
#13:48 13:59

#Solution 5% 35%
#%%
class Solution:
    def merge(self, intervals):
        intervals.sort()
        print(intervals)
        out = []
        res = []
        for i in intervals:
            if not len(res):
                res = i
            elif i[0] <= res[1]:
                res[1] = max(res[1],i[1])
            else:
                out.append(res)
                res = i
        if len(res):
            out.append(res)
        return out




# intervals = [[1,3],[2,6],[8,10],[15,18]]
# Solution().merge(intervals)
# #Output: [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
Solution().merge(intervals)
# Output: [[1,5]]