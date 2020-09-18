#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] restore-ip-addresses
#
class Solution(object):
    # def restoreIpAddresses(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     if len(s)<4 or len(s)>12:
    #         return []
    #     ans=[]
    #     for ia in range(1,len(s)):
    #         for ib in range(ia+1,len(s)):
    #             for ic in range(ib+1,len(s)):
    #                 segment=[str(int(i))==i and int(i)<=255 for i in [s[:ia],s[ia:ib],s[ib:ic],s[ic:]]]
    #                 if set(segment) == set([True]):
    #                     ans.append(''.join([s[:ia],'.',s[ia:ib],'.',s[ib:ic],'.',s[ic:]]))
    #     return ans
    def restoreIpAddresses(self, s):
        def backtrack(path, i, s):
            if len(path) == 4 and i == len(s):
                tmp = ''.join(x+'.' for x in path)
                res.append(tmp[:-1])
            if i < len(s):
                for j in range(3):
                    if i+j<len(s):
                        curr = s[i:i+j+1]
                        if int(curr) <= 255 and str(int(curr))==curr:
                            path.append(curr)
                            backtrack(path, i+j+1, s)
                            path.pop()
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        path = []
        backtrack(path, 0, s)
        return res
# @lc code=end