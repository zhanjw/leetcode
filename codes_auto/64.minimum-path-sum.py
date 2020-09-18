#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] minimum-path-sum
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i-1>=0 and j-1>=0:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
                if i-1>=0 and not j-1>=0:
                    grid[i][j]=grid[i-1][j]+grid[i][j]
                if not i-1>=0 and j-1>=0:
                    grid[i][j]=grid[i][j-1]+grid[i][j]
        return grid[-1][-1]
# @lc code=end