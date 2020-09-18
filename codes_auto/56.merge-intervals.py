#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] merge-intervals
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            elif intervals[i][1] > right:
                right = intervals[i][1]
        res.append([left, right])
        return res
# @lc code=end