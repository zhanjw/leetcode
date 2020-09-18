#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] product-of-array-except-self
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]
        right_dot=1
        for i in range(len(nums)):
            res.append(res[-1]*nums[i])
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*right_dot
            right_dot*=nums[i]
        return res[:-1]
# @lc code=end