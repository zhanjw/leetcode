#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] jump-game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0;
        for i in range(n):
            # 不断计算能跳到的最远距离
            farthest = max(farthest, i + nums[i])
            # 可能碰到了 0，卡住跳不动了
            if farthest <= i:
                break
        return farthest >= n-1
# @lc code=end