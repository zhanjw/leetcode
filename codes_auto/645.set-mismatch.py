#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] set-mismatch
#
from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dts=defaultdict(int)
        res=[-1,-1]
        for idx,num in enumerate(nums):
            dts[num]+=1
        for i in range(1,len(nums)+1):
            if dts[i]==2:
                res[0]=i
            if dts[i]==0:
                res[1]=i
        return res

# @lc code=end