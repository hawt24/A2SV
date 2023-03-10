# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def helper(node):
            if not node:
                return 
            helper(node.left)
            helper(node.right)
            dic[node.val]+=1
        helper(root)
        max_=0
        ans=[]
        for key,val in dic.items():
            if val>max_:
                max_=val
        for key, value in dic.items():
            if max_ == value:
                ans.append(key)
        return ans
            
        
            
        
