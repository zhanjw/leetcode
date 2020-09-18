#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] first-missing-positive
#
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)+1):
            visited=len(nums)-i+1
            while 0<nums[i-1]<=len(nums) and nums[i-1]!=i and visited>0:
                visited-=1
                n=nums[i-1]
                nums[i-1],nums[n-1]=nums[n-1],nums[i-1]
        print(nums)
        for i in range(1,len(nums)+1):
            if i!=nums[i-1]:
                return i
        return len(nums)+1
# @lc code=end