# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        
        if len(preorder)==1:
            return TreeNode(preorder[0])
            
        i=1
        for j in range(1, len(preorder)):
            if preorder[j]<preorder[0]:
                i+=1
                
        left=self.bstFromPreorder(preorder[1:i])
        right=self.bstFromPreorder(preorder[i:])
        
        return TreeNode(preorder[0], left=left, right=right)

      
        
        
        
        
        

        
   