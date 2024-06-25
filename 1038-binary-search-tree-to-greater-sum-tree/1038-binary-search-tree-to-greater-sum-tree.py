# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        self.sum=0
        def reverse_in_order(node):
            if not node:
                return
            reverse_in_order(node.right)
            self.sum+=node.val
            node.val=self.sum
            reverse_in_order(node.left)
        reverse_in_order(root)
        return root