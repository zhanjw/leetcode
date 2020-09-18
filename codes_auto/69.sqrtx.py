#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] sqrtx
#
import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        eps=1e-1
        x_i=1
        decreased = False;
        while True:
            # x_i_plus_1=(x_i+x/x_i)/2
            # if abs(x_i - x_i_plus_1) <= eps:
            #     x_i=x_i_plus_1
            #     break
            x_i_plus_1=(x_i+x/x_i)>>1
            if x_i==x_i_plus_1 or (x_i_plus_1 > x_i and decreased):
                break;
            decreased = (x_i_plus_1 < x_i)
            x_i=x_i_plus_1
        return x_i
            
# @lc code=end