# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def countPairs(self, root, distance):
        def dfs(node):
            if not node:
                return[]
        
            if not node.left and not node.right:
                return[1]  
            
            left_distances=dfs(node.left)
            right_distances=dfs(node.right)
            
           
            for ld in left_distances:
                for rd in right_distances:
                    if ld+rd<=distance:
                        self.count+=1
            
            return [d+1 for d in left_distances+right_distances if d+1<=distance]
        
        self.count=0
        dfs(root)
        return self.count