#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] water-and-jug-problem
#
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        if (z == 0):
            return True

        if (x == 0):
            return y == z

        if (y == 0):
            return x == z

        def gcd(a, b):
            smaller = min(a, b)
            while smaller:
                if a % smaller == 0 and b % smaller == 0:
                    return smaller
                smaller -= 1

        return z % gcd(x, y) == 0
# @lc code=end