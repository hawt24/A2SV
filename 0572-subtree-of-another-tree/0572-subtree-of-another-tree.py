# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
     
            if a.val!=b.val:
                return False
            l = helper(a.left,b.left)
            r = helper(a.right,b.right)
            return l and r
        
    
        ans=False
        def func(s,t):
            nonlocal ans
            if s and not ans: 
                if s.val==t.val:
                    ans =  helper(s,t)
                func(s.left,t)
                func(s.right,t)
        
        
        func(root,subRoot)
        return ans
    
            
            
            
            
        
