# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        temp=set()
        def dfs(node):
            nonlocal temp
            if not node:
                return
            temp.add(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        if len(temp)<2:
            return -1
        else:
            temp=sorted(list(temp))
            return temp[1]
      