#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] longest-substring-without-repeating-characters
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={}
        left,right=0,0
        max=0
        for i in range(len(s)):
            if s[i] in dicts and left<dicts[s[i]]+1:
                left=dicts[s[i]]+1
            right=i
            dicts[s[i]]=i
            if max<right-left+1:
                max=right-left+1
        return max
# @lc code=end