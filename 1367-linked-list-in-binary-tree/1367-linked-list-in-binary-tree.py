# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for singly-linked list.
class Solution(object):
    def isSubPath(self, head, root):
        def dfs(head, node):
            if not head:  
                return True
            if not node: 
                return False
            if head.val!=node.val:  
                return False
           
            return dfs(head.next,node.left) or dfs(head.next,node.right)
        if not root:  
            return False
        return dfs(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)