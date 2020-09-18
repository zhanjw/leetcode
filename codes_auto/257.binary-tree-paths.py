#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] binary-tree-paths
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        # if root.left is None and root.right is None:
        #     return [str(root.val)]
        # sub_paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        # return [str(root.val) + "->" + s for s in sub_paths]

        q = [root]
        tmp=[[]]
        res = []
        while q:
            node, pre_link = q.pop(0), tmp.pop(0)
            pre_link = pre_link + [str(node.val)]
            if node.left:
                q.append(node.left)
                tmp.append(pre_link)
            if node.right:
                q.append(node.right)
                tmp.append(pre_link)
            if not node.left and not node.right:
                res.append('->'.join(pre_link))
        return res
# @lc code=end