#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] maximal-square
#
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res=max(dp[i][j],res)
        return res**2
# @lc code=end