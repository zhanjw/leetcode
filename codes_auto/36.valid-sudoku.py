#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] valid-sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rule1=[set() for _ in range(9)]
        rule2=[set() for _ in range(9)]
        rule3=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] =='.':
                    continue
                if board[i][j] not in rule1[i]:
                    rule1[i].add(board[i][j])
                else:
                    return False
                if board[i][j] not in rule2[j]:
                    rule2[j].add(board[i][j])
                else:
                    return False
                z = i//3 * 3 + j//3
                if board[i][j] not in rule3[z]:
                    rule3[z].add(board[i][j])
                else:
                    return False
        return True
# @lc code=end