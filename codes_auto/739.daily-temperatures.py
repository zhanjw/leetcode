#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] daily-temperatures
#
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        l = len(T)
        stack = []
        res = [0] * l
        for idx, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                res[stack.pop()] = idx-stack[-1]
            stack.append(idx)
        return res

# @lc code=end