#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] coin-change
#
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        dp = [None for _ in range(amount+1)]
        for idx in range(len(dp)):
            for coin in coins:
                if idx%coin==0 and (not dp[idx] or dp[idx]>idx//coin):
                    dp[idx]=idx//coin
                if idx-coin>=0 and dp[idx-coin] and (not dp[idx] or dp[idx]>dp[idx-coin]+1):
                    dp[idx]=dp[idx-coin]+1
            # print(dp)
        return dp[-1] if dp[-1] else -1
# @lc code=end