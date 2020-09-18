#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] find-first-and-last-position-of-element-in-sorted-array
#
import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right=-1,-1
        if nums==[]:
            return(left,right)
        
        lo,hi=0,len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] < target: lo = mid+1
            else: hi = mid
        if len(nums)>lo and nums[lo]==target:
            left=lo
            lo,hi=left,len(nums)
        else:
            return(-1,-1)
        
        while lo < hi:
            mid = (lo+hi)//2
            if target < nums[mid]: hi = mid
            else: lo = mid+1
        if len(nums)>lo-1 and nums[lo-1]==target:
            right=lo-1
            
        return(left,right)
        
# @lc code=end