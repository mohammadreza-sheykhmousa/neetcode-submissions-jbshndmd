# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub:
            return True
        if not root:
            return False
        if self.isSametree(root, sub):
            return True
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)
            
    
    
    
    
    def isSametree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub and not root:
            return True
        if not sub or not root or sub.val != root.val:
            return False
        return self.isSametree(root.left, sub.left) and self.isSametree(root.right, sub.right)
        
        
        
        