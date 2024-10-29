# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self,root):
        arr = []
        self._inorderTraversal(root,arr) 
        return arr

    def _inorderTraversal(self,root,arr):
        if root is None:
            return
        self._inorderTraversal(root.left,arr)
        arr.append(root.val)
        self._inorderTraversal(root.right,arr)