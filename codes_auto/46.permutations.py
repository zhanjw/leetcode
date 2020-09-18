#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] permutations
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [[nums[0]]]
        res=[]
        for idx,num in enumerate(nums):
            rest=self.permute(nums[:idx]+nums[idx+1:])
            for i in rest:
                i.append(num)
                res.append(i)
        return res
# @lc code=end