# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        def traversal(node):
            if not node:
                return []
            return traversal(node.left)+[node.val]+traversal(node.right)
        sorted_values=traversal(root)
        
        def sorted_list(values):
            if not values:
                return None
            mid=len(values) // 2
            node=TreeNode(values[mid])
            node.left=sorted_list(values[:mid])
            node.right=sorted_list(values[mid+1:])
            return node
        return sorted_list(sorted_values)
       
        