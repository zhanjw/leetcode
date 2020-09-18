#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] two-sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt={}
        for i,val in enumerate(nums):
            if target-val in dt:
                return [dt[target-val],i]
            dt[val]=i
# @lc code=end