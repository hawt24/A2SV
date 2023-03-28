# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans=False
        currSum = 0
        
        def helper(node,s):
            nonlocal ans
            
            if node:
                s-=node.val
                
                if not node.left and not node.right and s==0:
                    ans=True
                    return 
                helper(node.left,s)
                helper(node.right,s)
        helper(root,targetSum)
        return ans
        