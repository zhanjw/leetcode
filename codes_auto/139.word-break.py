#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] word-break
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
        wordDict = set(wordDict)
        return self.getResult(s,wordDict,memo)
    def getResult(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if s in wordDict:
            memo[s]=True
            return True
        for idx in range(len(s)-1,-1,-1):
            if s[:idx+1] in wordDict:
                memo[s[:idx+1]]=True
                if self.getResult(s[idx+1:],wordDict,memo):
                    return True
        memo[s]=False
        return False

# @lc code=end