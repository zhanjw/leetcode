#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] search-a-2d-matrix-ii
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        j=0
        i=len(matrix)-1
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]>target:
                i-=1
            elif matrix[i][j]<target:
                j+=1
            else:
                return True
        return False
# @lc code=end