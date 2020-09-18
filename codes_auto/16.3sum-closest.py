#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 3sum-closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        margin=abs(res-target)
        for ida in range(len(nums)-2):
            idb=ida+1
            idc=len(nums)-1
            if abs((nums[ida]+nums[idb]+nums[idc])-target)<margin:
                res=nums[ida]+nums[idb]+nums[idc]
                margin=abs(res-target)
            while idb+1<idc:
                if nums[ida]+nums[idb]+nums[idc]<target:
                    idb+=1
                elif nums[ida]+nums[idb]+nums[idc]>target:
                    idc-=1
                elif nums[ida]+nums[idb]+nums[idc]==target:
                    return target
                if abs((nums[ida]+nums[idb]+nums[idc])-target)<margin:
                    res=nums[ida]+nums[idb]+nums[idc]
                    margin=abs(res-target)
        return res
# @lc code=end