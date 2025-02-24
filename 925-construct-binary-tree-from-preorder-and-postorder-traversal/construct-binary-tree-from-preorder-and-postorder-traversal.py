# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        left_root_val = preorder[1]
        left_subtree_size = postorder.index(left_root_val) + 1  
        
        root.left = self.constructFromPrePost(preorder[1:left_subtree_size+1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size+1:], postorder[left_subtree_size:-1])

        return root

def level_order_traversal(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

