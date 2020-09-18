#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] contains-duplicate
#
from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dts=defaultdict(int)
        for i in nums:
            dts[i]+=1
            if dts[i]>1:
                return True
        return False
# @lc code=end