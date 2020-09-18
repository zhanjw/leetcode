#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] partition-equal-subset-sum
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ & 1:
            return False
        target = sum_ / 2

        dp = [False]*(target+1)

        if nums[0] <= target:
            dp[nums[0]] = True
        dp[0] = True
        
        for i in range(1,len(nums)):
            for j in reversed(range(nums[i],target+1)):
                dp[j] = dp[j] or dp[j-nums[i]]
            if dp[-1]:
                return True
        return dp[-1]
# @lc code=end