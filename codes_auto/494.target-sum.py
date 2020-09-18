#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] target-sum
#
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = 0
        if nums and S <= 1000:
            dp = [[0 for i in range(2001)] for j in range(len(nums))]

            dp[0][1000 + nums[0]] += 1
            dp[0][1000 - nums[0]] += 1

            for i in range(1, len(nums)):
                for j in range(2001):
                    if dp[i - 1][j] > 0:
                        dp[i][j + nums[i]] += dp[i - 1][j]
                        dp[i][j - nums[i]] += dp[i - 1][j]

            res = dp[len(nums) - 1][S + 1000]

        return res
# @lc code=end