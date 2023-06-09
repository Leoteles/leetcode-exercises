#https://leetcode.com/problems/rotting-oranges/
#%%

#solution 73% 66%

class Solution:
    def orangesRotting(self, grid):
        fresh = {}
        rotten = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh[i,j] = 1
                elif grid[i][j] == 2:
                    rotten[i,j] = 1

        minutes = 0
        while fresh:
            just_rotted = []
            for i,j in fresh.keys():
                if ((i+1,j) in rotten) or ((i-1,j) in rotten) or ((i,j+1) in rotten) or ((i,j-1) in rotten):
                    just_rotted.append([i,j])
            for i,j in just_rotted:
                del fresh[i,j]
                rotten[i,j] = 1
            if not len(just_rotted):
                return -1
            minutes += 1
        return minutes



grid = [[2,1,1],[1,1,0],[0,1,1]]
#Output: 4
Solution().orangesRotting(grid)