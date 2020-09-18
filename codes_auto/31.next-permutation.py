#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] next-permutation
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums

        i=len(nums)-2
        while nums[i]>=nums[i+1] and i>-1:
            i-=1

        if i==-1:
            nums.sort()
            return

        j=i
        numj=max(nums)+1
        for k in range(len(nums)-1,i,-1):
            if nums[k]>nums[i] and nums[k]<numj:
                numj=nums[k]
                j=k
                
        nums[i],nums[j]=nums[j],nums[i]

        left=i+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

# @lc code=end