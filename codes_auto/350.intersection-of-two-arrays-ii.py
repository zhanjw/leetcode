#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] intersection-of-two-arrays-ii
#
from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        dts1=defaultdict(int)
        dts2=defaultdict(int)
        for i in nums1:
            dts1[i]+=1
        for i in nums2:
            dts2[i]+=1
        for i in set(nums1).intersection(set(nums2)):
            times=min(dts1[i],dts2[i])
            for _ in range(times):
                res.append(i)
        return res
# @lc code=end