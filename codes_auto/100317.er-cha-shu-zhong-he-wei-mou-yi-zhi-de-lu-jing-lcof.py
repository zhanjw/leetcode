#
# @lc app=leetcode.cn id=100317 lang=Python3
#
# [100317] er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def backtrace(root, curr_sum):
            if not root: return
            path.append(root.val)
            curr_sum -= root.val
            if curr_sum == 0 and not root.left and not root.right:
                res.append(list(path))
            backtrace(root.left, curr_sum)
            backtrace(root.right, curr_sum)
            path.pop()

        backtrace(root, sum)
        return res
# @lc code=end