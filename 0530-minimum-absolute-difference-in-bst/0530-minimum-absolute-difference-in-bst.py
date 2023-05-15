# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev_val = None
        min_diff = float('inf')
        
        def in_order_traversal(node):
            nonlocal prev_val, min_diff
            if not node:
                return
            
            in_order_traversal(node.left)
            if prev_val is not None:
                diff = abs(node.val - prev_val)
                if diff < min_diff:
                    min_diff = diff
            prev_val = node.val
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        return min_diff
        