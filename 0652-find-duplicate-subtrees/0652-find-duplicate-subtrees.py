# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[Optional[TreeNode]]:
        def dfs(node, subtrees):
            if not node:
                return False

            left = dfs(node.left, subtrees)
            right = dfs(node.right, subtrees)
            subtree = f"{node.val},{left},{right}"

            if subtree in subtrees:
                subtrees[subtree] += 1
            else:
                subtrees[subtree] = 1

            if subtrees[subtree] == 2:
                ans.append(node)

            return subtree

        ans = []
        dfs(root, defaultdict(int))
        return ans
