#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] length-of-last-word
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tail=len(s)-1
        while tail>=0 and s[tail] == " ":
            tail-=1
        head=tail
        while head>=0 and s[head] != " ":
            head-=1
        return tail-head
# @lc code=end