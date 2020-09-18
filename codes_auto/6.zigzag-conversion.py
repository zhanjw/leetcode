#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] zigzag-conversion
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows==0:
            return s 
        length=len(s)
        width=length//(numRows*2-2)*(numRows-1)
        block_idx=length%(numRows*2-2)
        if block_idx != 0:
            if block_idx <= (numRows-1):
                width=width+1
            else:
                width=width+block_idx-(numRows-1)
        height=numRows
        matrix = [[0 for i in range(width)] for j in range(height)]
        for i in range(len(s)):
            x=i//(numRows*2-2)*(numRows-1)+i%(numRows*2-2)//numRows
            y=i%(numRows*2-2)
            if x%(numRows-1)!=0:
                y=numRows-(y-(numRows-1))-1
            matrix[y][x]=s[i]
        output=""
        for i in matrix:
            for j in i:
                if j!=0:
                    output+=j
        return(output)
# @lc code=end