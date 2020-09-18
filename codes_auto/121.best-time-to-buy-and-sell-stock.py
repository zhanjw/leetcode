#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] best-time-to-buy-and-sell-stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit=0
        curr_buy=prices[0]
        for i in range(1,len(prices)):
            if curr_buy<prices[i]:
                max_profit=max(max_profit,prices[i]-curr_buy)
            else:
                curr_buy=prices[i]
        return max_profit
# @lc code=end