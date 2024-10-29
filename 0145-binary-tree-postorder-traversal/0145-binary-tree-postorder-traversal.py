# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        arr = []
        self._postorderTraversal(root,arr)  
        return arr

    def _postorderTraversal(self,root,arr):
        if root is None:
            return
        self._postorderTraversal(root.left,arr)
        self._postorderTraversal(root.right,arr)
        arr.append(root.val)