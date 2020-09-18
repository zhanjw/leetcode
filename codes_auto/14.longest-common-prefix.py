#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] longest-common-prefix
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common=""
        if strs:
            for i in range(len(strs[0])):
                common+=strs[0][i]
                for j in range(1,len(strs)):
                    if i>len(strs[j])-1:
                        return common[:-1]
                    if strs[0][i]!=strs[j][i]:
                        return common[:-1]
        return common
# @lc code=end