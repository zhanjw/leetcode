#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] sliding-window-maximum
#
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # if k<2:
        #     return nums
        window, res = [], []
        for i, val in enumerate(nums):
            if window and window[0] < i - k + 1:
                window.pop(0)
            while window and nums[window[-1]] < val:
                window.pop()
            window.append(i)
            res.append(nums[window[0]])
        return res[k-1:]
# @lc code=end