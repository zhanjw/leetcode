#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] subsets
#
class Solution(object):
    def subsets(self, nums):
        length = len(nums)
        res = []
        for i in range(2**length):
            index = length-1
            temp = []
            while index > -1:
                if i % 2 == 1:
                    temp.append(nums[index])
                index -= 1
                i = i >> 1
            res.append(temp)
        return res
# @lc code=end