#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] perfect-squares
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins=[]
        square_root=1
        new_coin=1
        while new_coin<=n:
            coins.append(new_coin)
            square_root+=1
            new_coin=square_root*square_root
        dp=[0 for _ in range(n+1)]
        for i in range(len(dp)):
            dp[i]=i
        for i in range(len(coins)):
            dp[coins[i]]=1
        for i in range(len(dp)):
            for j in range(len(coins)):
                if i-coins[j]>0 and dp[i]>dp[i-coins[j]]:
                    dp[i]=dp[i-coins[j]]+1
        return dp[-1]

# @lc code=end