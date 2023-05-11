# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def dfs(node,path,visited):
            nonlocal ans
            if not node:
                return 
            if node in visited:
                return 
            visited.add(node)
            new_path = path + str(node.val)
            if not node.left and not node.right:
                ans.append(new_path)
                return 
            dfs(node.left, new_path,visited)
            dfs(node.right, new_path,visited)
            
        dfs(root,'',set())
        total=0
        for i in ans:
            total+=int(i,2)
        return total
   
                
    