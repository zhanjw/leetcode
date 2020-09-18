#
# @lc app=leetcode.cn id=1086 lang=python
#
# [1086] divisor-game
#
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N%2==0:
            return True
        else:
            return False
# @lc code=end