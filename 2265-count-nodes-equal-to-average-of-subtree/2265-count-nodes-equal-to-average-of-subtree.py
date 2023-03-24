# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        cnt=0
        counter = 0
        def helper(node):
            nonlocal counter
            if not node:
                return [0,0]
            left=helper(node.left)
            right=helper(node.right)
            temp=[left[0]+right[0]+1,left[1] + right[1]+node.val]
            if temp[1] // temp[0] == node.val:
                counter += 1
            return temp
 

        helper(root)
        return counter


