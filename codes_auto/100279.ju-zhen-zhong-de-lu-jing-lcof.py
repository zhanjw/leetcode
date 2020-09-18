#
# @lc app=leetcode.cn id=100279 lang=Python3
#
# [100279] ju-zhen-zhong-de-lu-jing-lcof
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 暴力用dfs递归暴力查找：
        # 递归终止条件：
        #   False： 数组越界 or 当前索引和目标字符不匹配 
        #   True：传进来目标字符的索引=len(word)-1
        # 当前层递推：在上下左右四个方向进行递归；为了防止重复访问，标记当前元素，最后再重置元素；
        # 返回值：bool

        def dfs(i,j,k):
            if not (0 <= i < len(board)) or not(0 <= j < len(board[0])) or board[i][j] !=word[k]: return False
            if k == len(word)-1: return True
            temp, board[i][j] = board[i][j], "_" # 确保当前层不会重复访问
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = temp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): 
                    return True
        return False

# @lc code=end