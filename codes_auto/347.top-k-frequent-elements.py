#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] top-k-frequent-elements
#
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        buckets = [[] for _ in  range(len(nums) + 1)]
        
        for x, y in c.items():
            buckets[y].append(x)
        res = [] 
        i=len(nums)
        while i>0 and len(res)<k:
            if buckets[i]:
                res.extend(buckets[i])
            i-=1
        return res
# @lc code=end