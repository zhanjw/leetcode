#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] max-area-of-island
#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def setZero(i, j,area):
            grid[i][j]=0
            for d in directions:
                if 0<=i+d[0]<len(grid) and 0<=j+d[1]<len(grid[0]) and grid[i+d[0]][j+d[1]]==1:
                    setZero(i+d[0],j+d[1],area)
                    area[0]+=1

        max_area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=[1]
                    setZero(i,j,area)
                    max_area=max(area[0],max_area)
        return max_area
# @lc code=end