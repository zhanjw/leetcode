#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] shortest-unsorted-continuous-subarray
#
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length<=1:
            return 0

        left_max=[nums[0] for _ in range(length)]
        for i in range(1,length):
            left_max[i]=max(left_max[i-1],nums[i])

        right_min=[nums[-1] for _ in range(length)]
        for i in range(length-2,-1,-1):
            right_min[i]=min(right_min[i+1],nums[i])

        left,right = 0,length-1
        while left < length and right_min[left] == nums[left]:
            left += 1
        while right >= left + 1 and left_max[right] == nums[right]:
            right -= 1

        return right-left+1
# @lc code=end