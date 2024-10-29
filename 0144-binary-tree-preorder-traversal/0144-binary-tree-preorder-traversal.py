# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        arr = []
        self._preorderTraversal(root,arr)  
        return arr

    def _preorderTraversal(self,root,arr):
        if root is None:
            return
        arr.append(root.val)
        self._preorderTraversal(root.left,arr)
        self._preorderTraversal(root.right,arr)