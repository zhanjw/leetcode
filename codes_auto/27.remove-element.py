#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] remove-element
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # while val in nums:
        #     nums.remove(val)
        i=0
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
# @lc code=end