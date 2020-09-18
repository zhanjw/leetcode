#
# @lc app=leetcode.cn id=85 lang=python
#
# [85] maximal-rectangle
#
class Solution:
    def maximalRectangle(self, matrix):
        maxarea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': 
                    continue
                # compute the maximum width and update dp with it
                dp[i][j] = dp[i][j-1] + 1 if j else int(matrix[i][0])
                width = dp[i][j]
                maxarea = max(maxarea, width)
                # compute the maximum area rectangle with a lower right corner at [i, j]
                for previous_i in range(i-1, -1, -1):
                    width = min(width, dp[previous_i][j])
                    maxarea = max(maxarea, width * (i-previous_i+1))
        return maxarea
# @lc code=end