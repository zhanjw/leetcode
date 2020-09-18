#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] trapping-rain-water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        max_height=0
        max_height_index=0
        for idx,h in enumerate(height):
            if h>max_height:
                max_height=h
                max_height_index=idx
        left_water=0
        left_wall=0
        for i in range(0,max_height_index):
            if height[i]>left_wall:
                left_wall=height[i]
            else:
                left_water+=(left_wall-height[i])
        
        right_water=0
        right_wall=0        
        for i in range(len(height)-1,max_height_index,-1):
            if height[i]>right_wall:
                right_wall=height[i]
            else:
                right_water+=(right_wall-height[i])
        return left_water+right_water
# @lc code=end