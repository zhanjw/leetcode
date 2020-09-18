#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] number-of-islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def setZero(i, j):
            grid[i][j]='0'
            for d in directions:
                if 0<=i+d[0]<len(grid) and 0<=j+d[1]<len(grid[0]) and grid[i+d[0]][j+d[1]]=='1':
                    setZero(i+d[0],j+d[1])

        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    setZero(i,j)
                    count+=1
                # print(grid)
        return count
# @lc code=end