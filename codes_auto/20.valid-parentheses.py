#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] valid-parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        pair={"(":")","{":"}","[":"]"}
        stack=[]
        for i in s:
            if i in pair:
                stack.append(pair[i])
            elif stack and i==stack[-1]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
# @lc code=end