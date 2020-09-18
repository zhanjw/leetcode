#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] decode-string
#
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            stack.append(i)
            if i=="]":
                stack.pop(-1)
                curr_str=[]
                curr_pop=stack.pop(-1)
                while curr_pop!="[":
                    curr_str.extend(curr_pop)
                    curr_pop=stack.pop(-1)
                curr_times=[]
                while stack and stack[-1] in "0123456789":
                    curr_pop=stack.pop(-1)
                    curr_times.extend(curr_pop)
                times=int(''.join(curr_times[::-1]))
                for _ in range(times):
                    stack.extend(curr_str[::-1])
        return ''.join(stack)
# @lc code=end