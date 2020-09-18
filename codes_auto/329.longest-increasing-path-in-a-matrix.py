#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] longest-increasing-path-in-a-matrix
#
class Solution:
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix==[[]] or matrix==[]:
            return 0

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        rows=len(matrix)
        cols=len(matrix[0])
        len_path=1

        @lru_cache(None)
        def dfs(i,j):
            m_len_path=1
            for d in directions:
                if 0<=i+d[0]<rows and 0<=j+d[1]<cols and matrix[i+d[0]][j+d[1]]>matrix[i][j]:
                    m_len_path=max(m_len_path,dfs(i+d[0],j+d[1])+1)
            return m_len_path
            
        for i in range(rows):
            for j in range(cols):
                len_path=max(len_path,dfs(i,j))
        return len_path
# @lc code=end