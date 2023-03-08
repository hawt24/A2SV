# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def func(a,b):
            if a==None and b==None:
                return True
            elif a==None or b==None:
                return False
            elif a.val!=b.val:
                return False
            return func(a.left,b.left) and func(a.right,b.right)
        return func(p,q)