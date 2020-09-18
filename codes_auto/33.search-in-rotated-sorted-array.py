#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] search-in-rotated-sorted-array
#
import bisect
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        original_len=len(nums)
        if original_len==0 or original_len==1 and nums[0]!=target:
            return -1
        nums.extend(nums)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                i+=1
                break
        head=i
        tail=i+len(nums)//2-1
        target_index=bisect.bisect_left(nums,target,head,tail)
        if target_index>=len(nums) or nums[target_index]!=target:
            return -1
        if target_index>=original_len:
            return target_index-original_len
        return target_index
# @lc code=end