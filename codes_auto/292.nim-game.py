#
# @lc app=leetcode.cn id=292 lang=python
#
# [292] nim-game
#
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4==0:
            return False
        else:
            return True
# @lc code=end