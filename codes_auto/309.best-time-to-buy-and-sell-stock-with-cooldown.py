#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] best-time-to-buy-and-sell-stock-with-cooldown
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:
            return 0
        if n==2:
            count=prices[1]-prices[0]
            return count if count>0 else 0
        notHaving=n*[0]
        having=n*[0]
        having[0]=-prices[0]
        having[1]=max(notHaving[0]-prices[1],having[0])
        notHaving[1]=max(having[0]+prices[1],notHaving[0])
        for i in range(2,n):
            having[i]=max(notHaving[i-2]-prices[i],having[i-1])
            notHaving[i]=max(having[i-1]+prices[i],notHaving[i-1])
        return max(having[-1],notHaving[-1])
# @lc code=end