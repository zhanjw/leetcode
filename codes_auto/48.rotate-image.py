#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] rotate-image
#
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n//2):
            matrix[i],matrix[n-i-1]=matrix[n-i-1],matrix[i]
        for i in range(1,n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# @lc code=end