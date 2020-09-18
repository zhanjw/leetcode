#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] word-search
#
class Solution(object):
    direction=[(0,1),(1,0),(-1,0),(0,-1)]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)>len(board)*len(board[0]):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    first_char=board[i][j]
                    if self._dfs(board,word,i,j):
                        return True
                    board[i][j]=first_char
        return False
    def _dfs(self, board, word, i, j):
        # print(i,j,board)
        if board[i][j]==word[0]:
            if not word[1:]:
                return True
            board[i][j]=''
            for k in self.direction:
                curr_i=i+k[0]
                curr_j=j+k[1]
                if 0<=curr_i<len(board) and 0<=curr_j<len(board[0]):
                    temp=board[curr_i][curr_j]
                    if self._dfs(board, word[1:],curr_i,curr_j):
                        return True
                    board[curr_i][curr_j]=temp
        return False

# @lc code=end