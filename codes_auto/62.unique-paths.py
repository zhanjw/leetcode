#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] unique-paths
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result=[[1 for i in range(m)]for j in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                result[j][i]=result[j-1][i]+result[j][i-1]
        return result[-1][-1]
# @lc code=end