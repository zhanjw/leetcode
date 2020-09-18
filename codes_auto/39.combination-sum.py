#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] combination-sum
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        if target>0:
            if target in candidates:
                res.append([target])
            for idx,i in enumerate(candidates):
                search=self.combinationSum(candidates[idx:],target-i)
                for s in search:
                    s.append(i)
                    res.append(s)
        return res
# @lc code=end