#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] triangle
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp=[[] for i in range(len(triangle))]
        dp[0]=triangle[0]
        for i,rows in enumerate(triangle[1:],start=1):
            for j,val in enumerate(rows):
                if j==0:
                    dp[i].append(dp[i-1][j]+val)
                elif j==len(rows)-1:
                    dp[i].append(dp[i-1][j-1]+val)
                else:
                    dp[i].append(min(dp[i-1][j-1],dp[i-1][j])+val)
        return min(dp[-1])
# @lc code=end