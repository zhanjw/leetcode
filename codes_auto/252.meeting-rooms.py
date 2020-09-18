#
# @lc app=leetcode.cn id=252 lang=python
#
# [252] meeting-rooms
#
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])
        for idx in range(1,len(intervals)):
            if intervals[idx-1][1]>intervals[idx][0]:
                return False
        return True
# @lc code=end