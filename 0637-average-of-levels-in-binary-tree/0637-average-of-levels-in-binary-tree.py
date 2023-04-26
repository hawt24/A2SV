# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs(node):
            que=deque([node])
            ans=[]
            
            while que:
                total=0
                cur_level=len(que)
                
                for i in range(cur_level):
                    node=que.popleft()
                    total+=node.val
                    
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                        
                ans.append(total/cur_level)
                
            return ans
        return bfs(root)
        