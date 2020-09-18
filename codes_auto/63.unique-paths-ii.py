#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] unique-paths-ii
#
class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return 0
        
        len_of_i = len(grid)
        len_of_j = len(grid[0])
        dp = [[0 for x in range(len_of_j)] for y in range(len_of_i)] 
        
        for i in range(0, len_of_i):
            for j in range(0, len_of_j):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j-1]
                    if i - 1 >= 0:
                        dp[i][j] += dp[i-1][j]
                
        return dp[len_of_i-1][len_of_j-1]
# @lc code=end