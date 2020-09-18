#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] house-robber-ii
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)<=3:
            return max(nums)
        return max(self.rob198(nums[1:]),self.rob198(nums[:-1]))
    def rob198(self, nums):
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