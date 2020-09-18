#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] two-sum-ii-input-array-is-sorted
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dts={}
        for idx,number in enumerate(numbers):
            # print(idx,number,target-number,dts)
            if target-number in dts:
                return [dts[target-number],idx+1]
            dts[number]=idx+1
        return []
# @lc code=end