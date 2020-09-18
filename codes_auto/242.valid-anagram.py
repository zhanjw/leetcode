#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] valid-anagram
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dt={}
        for i in s:
            if i in dt:
                dt[i]+=1
            else:
                dt[i]=1
        for j in t:
            if j in dt:
                dt[j]-=1
                if dt[j]==0:
                    dt.pop(j)
            else:
                return False
        return True
# @lc code=end