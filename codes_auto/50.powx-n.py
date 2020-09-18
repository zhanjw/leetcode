#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] powx-n
#
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            # print(x, n)
            n >>= 1
        return pow
# @lc code=end