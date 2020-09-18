#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] house-robber
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=nums[:]
        for i in range(1,len(dp)):
            if i-2>=0:
                dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            else:
                dp[i]=max(nums[i],dp[i-1])
        return dp[-1]
# @lc code=end