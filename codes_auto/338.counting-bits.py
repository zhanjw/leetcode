#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] counting-bits
#
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res=[0]
        while len(res)<num+1:
            l=len(res)
            for j in range(l):
                res.append(1+res[j])
        return res[:num+1]
# @lc code=end