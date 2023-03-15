# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        level=[]
        que=[root]
        while que !=[] and root is not None:
            for node in que:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(node.val)
            que=level
            level=[]
        return ans
