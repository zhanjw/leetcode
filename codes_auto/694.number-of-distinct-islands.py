#
# @lc app=leetcode.cn id=694 lang=python3
#
# [694] number-of-distinct-islands
#
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def setZero(i, j,step,path):
            grid[i][j]=0
            for d in directions:
                if 0<=i+d[0]<len(grid) and 0<=j+d[1]<len(grid[0]) and grid[i+d[0]][j+d[1]]==1:
                    path=setZero(i+d[0],j+d[1],step+1,path)
                    path.append([step,d])
            return path

        count=0
        path=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    tmp=[]
                    tmp=setZero(i,j,0,tmp)
                    # print(i,j,tmp)
                    if tmp not in path:
                        path.append(tmp)
                        count+=1
        return count
# @lc code=end