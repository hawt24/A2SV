# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt=0
        dic={0:1}
        def helper(node,preSum):
            nonlocal cnt
            if not node:
                return 
            currSum=preSum+node.val
            diff=currSum-targetSum
            if diff in dic:
                cnt+=dic[diff]
            if currSum in dic:
                dic[currSum]+=1
            else:
                dic[currSum]=1
            helper(node.left,currSum)
            helper(node.right,currSum)
            dic[currSum]-=1
        helper(root,0)
        return cnt
        