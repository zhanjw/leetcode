#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] hamming-distance
#
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count=0
        while x or y:
            if x%2 != y%2:
                count+=1
            x=x>>1
            y=y>>1
            # print(x,y)
        return count
# @lc code=end