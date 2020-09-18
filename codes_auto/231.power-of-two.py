#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] power-of-two
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n==1 or n==2:
            # return True
        while n>=2.0:
            n/=2.0
        if n==1.0:
            return True
        else:
            return False
# @lc code=end