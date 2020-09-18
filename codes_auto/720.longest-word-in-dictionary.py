#
# @lc app=leetcode.cn id=720 lang=python
#
# [720] longest-word-in-dictionary
#
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        valid = set([""])
        for word in sorted(words, key=len):
            if word[:-1] in valid:
                valid.add(word)
        return max(sorted(valid), key=len)
# @lc code=end