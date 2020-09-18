#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] subsets-ii
#
from collections import defaultdict
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1

        res = [[]]
        for key, value in dic.items():
            temp = res[:]
            for idx,data in enumerate(res):
                for times in range(value):
                    _temp=[data+[key]*(times+1)]
                    temp.extend(_temp)
            res = temp
        return res
# @lc code=end