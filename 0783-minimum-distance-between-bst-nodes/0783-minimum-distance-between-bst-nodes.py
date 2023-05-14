# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.dfs(root, res)
        ans = float("inf")
        for i in range(1, len(res)):
            ans = min(ans, abs(res[i]-res[i-1]))
        return ans

    def dfs(self,node,res):
        if node:
            self.dfs(node.left,res)
            res.append(node.val)
            self.dfs(node.right,res)