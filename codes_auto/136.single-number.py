#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] single-number
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans^=i
        return ans
# @lc code=end