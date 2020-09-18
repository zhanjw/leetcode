#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] reverse-words-in-a-string-iii
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_split=s.split(" ")
        for index,i in enumerate(s_split):
            s_split[index]=i[::-1]
            s_split[index]+=" "
        return ''.join(s_split)[:-1]
# @lc code=end