# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=[]
        curr=head
        n=0
        while curr:
            temp.append(curr.val)
            n+=1
            curr=curr.next
        ans=0
        for i in range(n//2):
            ans=max(ans,temp[i]+temp[n-1-i])
        return ans
            
            
        