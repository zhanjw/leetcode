#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] best-time-to-buy-and-sell-stock-ii
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        earn=0
        hold=None
        for i in prices:
            # if hold==None:
            #     hold=i
            if hold!=None and i>hold:
                earn+=i-hold
            hold=i
        return earn
# @lc code=end