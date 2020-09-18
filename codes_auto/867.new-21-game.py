#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] new-21-game
#
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1] * (N + 1)
        cur = 0
        for i in range(1, N + 1):
            if i <= K:
                cur += dp[i - 1]
            if K + W >= i > W:
                cur -= dp[i - 1 - W]
            dp[i] = cur / W
        return sum(dp[K:])
# @lc code=end