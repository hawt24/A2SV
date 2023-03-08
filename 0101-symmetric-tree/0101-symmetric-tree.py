# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # arr,arr1=[],[]
        # def inorderleft(node,arr):
        #     if node is None:
        #         #arr.append(None)
        #         return 
        #     inorderleft(node.left,arr)
        #     arr.append(node.val)
        #     if node.right:
        #         inorderleft(node.right,arr)
        #     else:
        #         arr.append(None)
        # inorderleft(root.left,arr)
        # def inorderright(node,arr1):
        #     if node is None:
        #         #arr1.append(None)
        #         return 
        #     inorderright(node.right,arr1)
        #     arr1.append(node.val)
        #     inorderright(node.left,arr1)
        # inorderright(root.right,arr1)
        # print(arr,arr1)
        # if arr==arr1:
        #     return True
        # return False
        def cheker(a,b):
            if a==None and b==None:
                return True
            if a==None or b==None:
                return False
            return a.val==b.val and cheker(a.left,b.right) and cheker(a.right,b.left)
        return cheker(root,root)
        
            


           
          
            


