#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] binary-tree-level-order-traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue=[[root]]
        res=[[root.val]]
        while queue:
            curr_layer=queue.pop()
            layer=[]
            tmp_res=[]
            for curr in curr_layer:
                if curr.left:
                    layer.append(curr.left)
                    tmp_res.append(curr.left.val)
                if curr.right:
                    layer.append(curr.right)
                    tmp_res.append(curr.right.val)
            if len(layer)>0:
                queue.append(layer)
                res.append(tmp_res)
        return res
            
# @lc code=end