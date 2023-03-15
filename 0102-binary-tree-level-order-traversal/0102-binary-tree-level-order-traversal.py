# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        level=[]
        que=[root]
        
        while que !=[] and root is not None:
            temp=[]
            for node in que:
                temp.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(temp)
            que=level
            level=[]
        return ans
 


            