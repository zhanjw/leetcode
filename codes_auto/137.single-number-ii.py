#
# @lc app=leetcode.cn id=137 lang=python
#
# [137] single-number-ii
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = [0] * 32
        for num in nums:
            for i in xrange(32):
                bit[i] += num >> i & 1
        res = 0
        print(bit)
        for i, val in enumerate(bit):
            # if the single numble is negative,
            # this case should be considered separately 
            if i == 31 and val%3:
                res = -((1<<31)-res)
            else:
                res |= (val%3)*(1<<i)
        return res
# @lc code=end