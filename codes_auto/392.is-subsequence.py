#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] is-subsequence
#
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ps=0
        pt=0
        while pt<len(t):
            if s[ps]==t[pt]:
                if ps==len(s)-1:
                    return True
                ps+=1
                pt+=1
            else:
                pt+=1
        return False
# @lc code=end