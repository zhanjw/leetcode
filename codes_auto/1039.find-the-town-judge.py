#
# @lc app=leetcode.cn id=1039 lang=python
#
# [1039] find-the-town-judge
#
class Solution(object):
    def findJudge(self, N, trust):
        if not trust:
            return N
        dt={}
        obj=set([])
        for i in trust:
            obj.add(i[0])
            if i[1] not in dt:
                dt[i[1]]=1
            else:
                dt[i[1]]+=1
        for k,v in dt.items():
            if (v==N-1) and (len(obj)==N-1):
                return k
        return -1
# @lc code=end