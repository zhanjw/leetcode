#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] find-all-numbers-disappeared-in-an-array
#
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        res=[]
        for idx,num in enumerate(nums):
            if num>0:
                res.append(idx+1)
        return res
# @lc code=end