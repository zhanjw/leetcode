#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] koko-eating-bananas
#
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def timeOf(n, speed):
            if n%speed>0:
                return n // speed + 1
            else:
                return n // speed

        def finishtime(speed):
            time = 0;
            for n in piles:
                time += timeOf(n, speed)
            return time

        left=1
        right=max(piles)
        while left<right:
            middle=(left+right)//2
            if finishtime(middle)<=H:
                right=middle
            else:
                left=middle+1
        return left
# @lc code=end