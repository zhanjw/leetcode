#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] group-anagrams
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts={}
        res=[]
        for i in strs:
            uid=''.join(sorted(list(i)))
            if uid not in dicts:
                dicts[uid]=[i]
            else:
                dicts[uid].append(i)
        for i in dicts:
            res.append(dicts[i])
        return res
# @lc code=end