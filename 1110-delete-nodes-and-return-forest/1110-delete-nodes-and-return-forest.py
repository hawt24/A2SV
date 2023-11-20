# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, is_root):
            if not node:
                return None

            left_val = dfs(node.left, False)
            right_val = dfs(node.right, False)

            if node.val in to_delete:
                if left_val:
                    ans.append(left_val)
                if right_val:
                    ans.append(right_val)
                return None

            if is_root:
                ans.append(node)

            node.left = left_val
            node.right = right_val

            return node

        ans = []
        dfs(root, True)
        return ans
            
                
            
                
        