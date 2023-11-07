# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node)
            inorder(node.right)
        inorder(root)
        
        first_node, second_node = None, None
        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                if first_node is None:
                    first_node = arr[i]
                second_node = arr[i + 1]
        
        first_node.val, second_node.val = second_node.val, first_node.val
            
    