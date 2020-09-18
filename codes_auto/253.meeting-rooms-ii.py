#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] meeting-rooms-ii
#
import heapq

class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        events = [(i[0], 1) for i in intervals] + [(i[1], -1) for i in intervals]
        events.sort()
        ans = cur = 0
        for _, op in events:
            cur += op
            ans = max(ans, cur)
        return ans

        # rooms = []  # 记录各会议室的最早结束时间
        # meetings = sorted(intervals, key=lambda x: x[0])  # 按开始时间升序
        # for meeting in meetings:
        #     # 如果最早结束的会议室的结束时间比会议室时间要早，则先关闭该会议室
        #     if rooms and rooms[0] <= meeting[0]:
        #         heapq.heappop(rooms)
        #     # 插入新的会议室到最小堆
        #     heapq.heappush(rooms, meeting[1])
        # return len(rooms)

# @lc code=end