# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def delNodes(self,root,to_delete):
        to_delete_set=set(to_delete)
        res=[]
        
        def forest(node, is_root):
            if not node:
                return None
            root_deleted=node.val in to_delete_set
            if is_root and not root_deleted:
                res.append(node)
            node.left=forest(node.left,root_deleted)
            node.right=forest(node.right,root_deleted)
            return None if root_deleted else node
        
        forest(root, True)
        return res