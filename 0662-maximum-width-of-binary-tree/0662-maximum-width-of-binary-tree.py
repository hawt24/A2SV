# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=1
        que=[(root,0)]
        while len(que)!=0:
            if len(que)>1:
                ans=max(ans,que[-1][1]-que[0][1]+1)
            temp=[]
            while len(que)!=0:
                root,idx=que.pop(0)
                if root.left:
                    temp.append((root.left,idx*2))
                if root.right:
                    temp.append((root.right,idx*2+1))
            que=temp
        return ans
            
        
            