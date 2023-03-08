# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        
        def helper(node):
            nonlocal ans
            if node is None:
                return 0
            
            left=helper(node.left)
            right=helper(node.right)
            
            if abs(left-right)>1:
                ans=False
            
            return 1+max(left,right)
        
        helper(root)
        
        return ans