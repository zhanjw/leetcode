#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] search-insert-position
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)
        while l<r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            else:
                r=m
            print(m)
        return l
# @lc code=end