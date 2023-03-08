# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr=[]
        def helper(node,st=[]):
            if node is None:
                return 
            if node.left is None and not node.right:
                arr.append("->".join(st+[str(node.val)]))
                return 
            
            left=helper(node.left,st+[str(node.val)])
            right=helper(node.right,st+[str(node.val)])
        helper(root)
        return arr