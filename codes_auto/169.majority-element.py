#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] majority-element
#
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cts=Counter(nums)
        return cts.most_common(1)[0][0]

# @lc code=end