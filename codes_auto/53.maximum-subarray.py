#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] maximum-subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = nums[:]  # 初始化dp数组，dp[i]存储以nums[i]为结尾的子数组的和的最大值
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])  # 更新dp[i]
        res = max(dp) # 更新全局最大值
        return res
# @lc code=end