#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] reverse-integer
#
class Solution(object):
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
        strx=str(abs(x))
        intx=int(strx[::-1])
        if (intx<-(2**31) or intx>(2**31)-1):
            return 0
        return sign*intx
# @lc code=end