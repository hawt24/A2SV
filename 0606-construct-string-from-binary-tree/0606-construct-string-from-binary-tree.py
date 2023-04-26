# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.preorder(root)
    
    def preorder(self,root):
        
        if not root:
            return 
        
        if not root.right and not root.left:
            return str(root.val)
        
        l = self.preorder(root.left)
        r = self.preorder(root.right)
        
        ans =str(root.val)
        
        if l:
            ans+= ("(" + l + ")")
        else:
            ans+= ("()")
        if r:
            ans+=("(" + r + ")")
        return ans

        