#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] climbing-stairs
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre,cur=0,1
        for i in range(n):
            pre,cur=cur,pre+cur
        return cur
# @lc code=end