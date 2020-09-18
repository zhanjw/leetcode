#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] convert-bst-to-greater-tree
#
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
# @lc code=end