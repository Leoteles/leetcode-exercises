# https://leetcode.com/problems/number-of-islands/

#Solution 70% 44%

class Solution:
    def dfs(self,i,j,grid):
        #Off board
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])):
            return
        if grid[i][j]=='1':
            grid[i][j] ='-1' #mark as visited
            self.dfs(i+1,j,grid)
            self.dfs(i-1,j,grid)
            self.dfs(i,j+1,grid)
            self.dfs(i,j-1,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == '1':
                    self.dfs(i,j,grid)
                    out += 1
        return out
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Solution().numIslands(grid)
