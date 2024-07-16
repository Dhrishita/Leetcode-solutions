# Definition for a binary tree node.class TreeNode:
def __init__(self, val=0, left=None, right=None):
    self.val=val
    self.left=left
    self.right=right

class Solution(object):
    def getDirections(self,root,startValue,destValue):
        def findPath(root,value,path):
            if not root:
                return False
            if root.val==value:
                return True
            path.append('L')
            if findPath(root.left,value,path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right,value,path):
                return True
            path.pop()
            return False
        
        def findLCA(root,p,q):
            if not root or root.val==p or root.val==q:
                return root
            left=findLCA(root.left,p,q)
            right=findLCA(root.right,p,q)
            if left and right:
                return root
            return left if left else right
        
        startPath=[]
        destPath=[]
        findPath(root,startValue,startPath)
        findPath(root,destValue,destPath)
        
     
        lca = findLCA(root,startValue,destValue)
        lcaToStart=[]
        findPath(lca,startValue,lcaToStart)
        lcaToDest=[]
        findPath(lca,destValue,lcaToDest)
        
        upSteps='U'*len(lcaToStart)
        result=upSteps+''.join(lcaToDest)
        
        return result