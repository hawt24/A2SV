# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        return self.rob_helper(root, memo)

    def rob_helper(self, root, memo) -> int:
        if not root:
            return 0
        if root in memo:
            return memo[root]

        sum1 = root.val
        sum2 = 0

        if root.left:
            sum1 += self.rob_helper(root.left.left, memo) + self.rob_helper(root.left.right, memo)
        if root.right:
            sum1 += self.rob_helper(root.right.left, memo) + self.rob_helper(root.right.right, memo)

        sum2 = self.rob_helper(root.left, memo) + self.rob_helper(root.right, memo)

        memo[root] = max(sum1, sum2)

        return memo[root]
        