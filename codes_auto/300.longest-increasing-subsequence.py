#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] longest-increasing-subsequence
#
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp=[1 for i in nums]
        for i,vali in enumerate(nums):
            for j,valj in enumerate(nums):
                if i<j and vali<valj:
                    dp[j]=max(dp[j],dp[i]+1)
        return max(dp)
# @lc code=end